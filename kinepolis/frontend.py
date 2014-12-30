from etc import *
from classes import *
from datastruct import *

import npyscreen

import traceback
import random
import datetime

kinepolis_logo_footer="""


To exit, press CTRL+X.

Please make your choice:

"""

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
        log()
        print("goodbye")
    
    print(log_string)


# Own widget classes ----------------------------------------------------

class NoBullShitText(npyscreen.Pager):
    def __init__(self, *args, **kwargs):
        kwargs["height"] = kwargs["text"].count("\n")+1
        kwargs["values"] = kwargs["text"].split("\n")
        kwargs["name"] = "no bullshit please"
        kwargs["autowrap"] = True
        kwargs["editable"] = False
        del(kwargs["text"])
        
        npyscreen.Pager.__init__(self, *args, **kwargs)
        
# this class is not a form, it's a widget that should be displayed in the form ViewShowsList
class ViewShows(npyscreen.MultiLineAction):
    def __init__(self, *args, **kwargs):
        super(ViewShows, self).__init__(*args, **kwargs)
        self.add_handlers({
            "^X": self.exit
        })
    
    def display_value(self, vl):
        return str(vl)
    
    # passes the call onto the parent
    def actionHighlighted(self, selected_show, keypress):
        self.parent.on_element_selected(selected_show, keypress)
    
    def exit(self, whatever):
        self.parent.parentApp.switchForm("MAIN")


class ViewShowsList(npyscreen.Form):
    def create(self):
        self.wgTitle = self.add(NoBullShitText, text="Pick a Show.\nTo exit, press CTRL+X.\n")
        self.wgShows = self.add(ViewShows)
    
    def beforeEditing(self):
        self.update_list()
    
    def update_list(self):
        self.wgShows.values = list(self.parentApp.cinema.shows.sort("ID"))
        #self.wMain.values = [1, 2, 3]
        self.wgShows.display()
    
    # careful, the self parameter will contain the form, not the widget!
    def on_element_selected(self, selected_show, keypress):
        # override me!
        pass

# EnterTheater ---------------------------------------------------------

class PickShowToEnter(ViewShowsList):
    def on_element_selected(self, selected_show, keypress):
        selected_show.popTicket()
        if selected_show.isEmptyTickets():
            npyscreen.notify_confirm("The film can start!")
            # TODO Star Wars easter egg here
        else:
            npyscreen.notify_confirm("We still need "+str(selected_show.tickets.length)+" people "\
                + "for the film \n   '" + selected_show.film.title+ "'.")
        self.update_list()

# Shows ----------------------------------------------------------------

class PickShowReservation(ViewShowsList):
    def on_element_selected(self, selected_show, keypress):
        log("make reservation?")
        self.parentApp.getForm("MAKERESERVATION").show = selected_show
        self.parentApp.switchForm("MAKERESERVATION")


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
        if self.value != '':
            try:
                i = int(self.value)
            except:
                npyscreen.notify_confirm("Not a valid integer, try again!")


class MakeReservation(npyscreen.ActionForm):
    def __init__(self, *args, **kwargs):
        super(MakeReservation, self).__init__(*args, **kwargs)
        self.add_handlers({
            "^X": self.on_cancel
        })
    
    def create(self):
        self.show = None  # please overwrite me with the show we are getting tickets for
        
        self.wgTitle = self.add(NoBullShitText, text="You are buying tickets for this show:\nSHOW HERE\n\n")
        
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

        # reset all values
        for toreset in [self.wgUserMail, self.wgUserFirstname, self.wgUserLastname, self.wgResPlaces]:
            toreset.value = ''
    
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
                # ID is really awkward, because we don't use it anymore
                hash(self.wgUserMail.value),
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
        self.parentApp.switchForm("PICKSHOWRESERVATION")
        
    def on_cancel(self, whatever=None):
        # simply switch to the previous form
        self.parentApp.switchForm("PICKSHOWRESERVATION")


# Main menu -------------------------------------------------------

class MakeReservationButton(npyscreen.ButtonPress):
    def whenPressed(self):
        # this is a widget, so don't just call self.parentApp!
        self.parent.parentApp.switchForm("PICKSHOWRESERVATION")


class EnterTheaterButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm("PICKSHOWTOENTER")


class MainMenu(npyscreen.Form):
    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)
        self.add_handlers({
            "^X": self.exit
        })
    
    def create(self):
        #self.add(NoBullShitText, name="Please make your choice.\n")
        log("creating MainMenu")

        self.add(NoBullShitText, text=fancytext(self.parentApp.cinema.name)+kinepolis_logo_footer)
        self.add(MakeReservationButton, name="Make a reservation")
        self.add(EnterTheaterButton, name="Enter theater")
   
    def exit(self, whatever):
        self.parentApp.switchForm(None)

# THE APP ---------------------------------------------------------

class MyCinemaApp(npyscreen.NPSAppManaged):
    def __init__(self, cinema):
        npyscreen.NPSAppManaged.__init__(self)
        self.cinema = cinema
        
    def onStart(self):
        self.addForm("MAIN", MainMenu)
        self.addForm("PICKSHOWRESERVATION", PickShowReservation)
        self.addForm("PICKSHOWTOENTER", PickShowToEnter)
        self.addForm("MAKERESERVATION", MakeReservation)
