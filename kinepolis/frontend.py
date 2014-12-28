from etc import *
from classes import *
from datastruct import *

import npyscreen

import traceback
import random
import datetime

log_string = ""

def log(s="****ERROR****"):
    global log_string
    if s=="****ERROR****":
        s = traceback.format_exc()
    log_string += s + "\n"

def start_frontend(data):
    cin_name = ""
    while True:
        cin_name = input("Cinema name? [kinepolis]\n"+rgbtext("> ", green))
        if cin_name == "": cin_name = "kinepolis"
        if cin_name in data and type(data[cin_name]) == Cinema:
            break
        print(rgbtext("404: Cinema not found.", red))
    
    print(rgbtext("Loading cinema {}".format(cin_name), green))
    cin = data[cin_name]
    
    app = MyCinemaApp(cin)
    try:
        app.run()
    except:
        print("goodbye")
    
    print(log_string)


# Own widget classes ----------------------------------------------------
"""
class NoBullShitText(npyscreen.widget.Widget):  
    def calculate_area_needed(self):
        return (self.name.count("\n")+1, 0)
    
    editable = False
    
    def update(self, clear=False): # no one cares about clear
        i = 0
        for line in self.name.split("\n"):
            self.add_line(self.rely+i, self.relx,
                line,
                self.make_attributes_list(line, 2048),
                len(line) # label width?
                )
            i+=1
"""

class NoBullShitText(npyscreen.Pager):
    def __init__(self, *args, **kwargs):
        kwargs["height"] = kwargs["text"].count("\n")+1
        kwargs["values"] = kwargs["text"].split("\n")
        kwargs["name"] = "no bullshit please"
        kwargs["autowrap"] = True
        kwargs["editable"] = False
        del(kwargs["text"])
        
        npyscreen.Pager.__init__(self, *args, **kwargs)


# Shows ----------------------------------------------------------------

# this class is not a form, it's a widget that should be displayed in the form ViewShowsList
class ViewShows(npyscreen.MultiLineAction):
    def __init__(self, *args, **kwargs):
        log("created ViewShows")
        super(ViewShows, self).__init__(*args, **kwargs)
        self.add_handlers({
            "^X": self.exit
        })
        log("end of createing viewshows")
    
    def display_value(self, vl):
        return str(vl)
    
    def actionHighlighted(self, selected_show, keypress):
        self.parent.parentApp.getForm("MAKERESERVATION").show = selected_show
        self.parent.parentApp.switchForm("MAKERESERVATION")
    
    #def when_add_user(self, *args, **keywords):
        #self.parent.parentApp.getForm('EDITUSER').value = None
        #self.parent.parentApp.switchForm('EDITUSER')
    
    #def when_delete_user(self, *args, **kwargs):
        #self.parent.parentApp.myDatabase.pop(self.values[self.cursor_line].ID)
        #self.parent.update_list()
    
    def exit(self, whatever):
        self.parent.parentApp.switchForm(None)


class ViewShowsList(npyscreen.Form):
    def create(self):
        self.wgTitle = self.add(NoBullShitText, text="Pick a Show.\nTo exit, press CTRL+C.\n")
        self.wgShows = self.add(ViewShows)
    
    def beforeEditing(self):
        self.update_list()
    
    def update_list(self):
        self.wgShows.values = list(self.parentApp.cinema.shows.sort("ID"))
        #self.wMain.values = [1, 2, 3]
        self.wgShows.display()

class MagicalUserMail(npyscreen.TitleText):
    def on_leave(self):
        # this method gets called whenever people leave the user mail field
        # the purpose of this method is automatically inserting user details
        # when the user mail is already in our system!
        log("super epic autocomplete!")
        
        user = self.parent.parentApp.cinema.users.retrieve(self.value)
        if user != None:
            log("found user "+str(user))
            self.parent.wgUserFirstname.value = user.firstname
            self.parent.wgUserLastname.value = user.lastname

class IntegerTitleText(npyscreen.TitleText):
    def on_leave(self):      
        try:
            i = int(self.value)
        except:
            npyscreen.notify_confirm("Not a valid integer, try again!")

class MakeReservation(npyscreen.ActionForm):
    def create(self):
        self.show = None  # please overwrite me with the show we are getting tickets for
        
        self.wgTitle = self.add(NoBullShitText, text="You are buying tickets for:\nSHOW HERE\n\n")
        
        # User stuff
        self.add(NoBullShitText, text="Please provide some info about yourself:\n")
        self.wgUserMail = self.add(MagicalUserMail, name="Mail")
        self.wgUserFirstname = self.add(npyscreen.TitleText, name="First name")
        self.wgUserLastname = self.add(npyscreen.TitleText, name="Last name")
        
        # Reservation stuff
        # ID, user, timeStamp, show, places
        self.add(NoBullShitText, text="\n\nDetails about your reservation:\n")
        self.wgResPlaces = self.add(IntegerTitleText, name="Places")
    
    
    def beforeEditing(self):
        # Basically, after creating a NoBullShitText widget, it behaves like a Pager
        self.wgTitle.values[1] = str(self.show)
        
        # TODO
        # reset all values
        for toreset in [self.wgUserMail, self.wgUserFirstname, self.wgUserLastname, self.wgResPlaces]:
            toreset.value = ''
        
        """if self.value: # editing, not creating
            show = self.parentApp.cinema.shows.retrieve(self.value)
            
            self.name = "Show ID: {}".format(show.ID)
            self.show_ID = show.ID
            self.wgID.value = show.ID
            self.wgTitle.value = show.film.title
            #self.wgFirstname.value = record.firstname
            #self.wgLastname.value = record.lastname
            #self.wgEmail.value = record.mail
        else:
            self.name = "New Show, wtf"
            self.show_id = 0
            self.wgID.value = 0
            self.wgTitle.value = ""
        """
    
    
    def on_ok(self):
        # user stuff
        # we update or insert the user
        if self.wgUserMail.value == '' or self.wgUserFirstname.value == '' or \
            self.wgUserLastname.value == '' or self.wgResPlaces.value == '':
            npyscreen.notify_confirm("Please fill in all the fields")
            return
        
        user = self.parentApp.cinema.users.retrieve(self.wgUserMail.value)
        if user == None:
            # inserting
            # user init:
            # ID, firstname, lastname, mail
            user = User(
                # ID is really awkward, because we don't really use it anymore
                random.randint(1000,2000),
                self.wgUserFirstname.value,
                self.wgUserLastname.value,
                self.wgUserMail.value
                )
            self.parentApp.cinema.users.insert(user)
        else:
            # updating
            user.firstname = self.wgUserFirstname.value
            user.lastname = self.wgUserLastname.value
        
        # first of all, make sure that self.wgResPlaces is a valid integer
        places = 0
        try:
            places = int(self.wgResPlaces.value)
        except:
            npyscreen.notify_confirm("Not a valid integer, try again!")
            return
        
        # reservation init:
        # ID, user, timeStamp, show, places
        reservation = Reservation(
            # determining the ID is *really* awkward
            self.parentApp.cinema.reservationCounter,
            user,
            datetime.datetime.now(),
            self.show,
            places)
        
        # enqueue the reservation
        if not self.parentApp.cinema.addReservation(reservation):
            # the reservation was invalid
            npyscreen.notify_confirm("We don't have that many places available.")
            return
        
        # and switch back
        self.parentApp.switchForm("VIEWSHOWS")
        
    def on_cancel(self):
        # simply switch to the previous form
        self.parentApp.switchForm("VIEWSHOWS")


# Main menu -------------------------------------------------------

class MakeReservationButton(npyscreen.ButtonPress):
    def whenPressed(self):
        # this is a widget, so don't just call self.parentApp!
        self.parent.parentApp.switchForm("VIEWSHOWS")


class EnterTheaterButton(npyscreen.ButtonPress):
    def whenPressed(self):
        npyscreen.notify_confirm("Entering theater...")


class MainMenu(npyscreen.Popup):
    def create(self):
        #self.add(NoBullShitText, name="Please make your choice.\n")
        log("creating MainMenu")

        self.add(NoBullShitText, text="test\nnewline!\nanother one!")
        self.add(MakeReservationButton, name="Make a reservation")
        self.add(EnterTheaterButton, name="Enter theater")

# THE APP ---------------------------------------------------------

class MyCinemaApp(npyscreen.NPSAppManaged):
    def __init__(self, cinema):
        npyscreen.NPSAppManaged.__init__(self)
        self.cinema = cinema
        
    def onStart(self):
        self.addForm("MAIN", MainMenu)
        self.addForm("VIEWSHOWS", ViewShowsList)
        self.addForm("MAKERESERVATION", MakeReservation)
