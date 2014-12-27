from etc import *
from classes import *
from datastruct import *

import npyscreen

import traceback

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


class MakeReservation(npyscreen.ActionForm):
    def create(self):
        self.show = None  # please overwrite me with the show we are getting tickets for
        
        self.wgTitle = self.add(NoBullShitText, text="You are buying tickets for:\nSHOW HERE\n\n")
        
        # User stuff
        self.add(NoBullShitText, text="Please provide some info about yourself:\n")
        self.wgUserMail = self.add(npyscreen.TitleText, name="Mail")
        self.wgUserFirstname = self.add(npyscreen.TitleText, name="First name")
        self.wgUserLastname = self.add(npyscreen.TitleText, name="Last name")
        
        # Reservation stuff
    
    
    def beforeEditing(self):
        # Basically, after creating a NoBullShitText widget, it behaves like a Pager
        self.wgTitle.values[1] = str(self.show)
        
        # TODO
        # reset all values
        
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
        npyscreen.notify_confirm("heya there")
        
    def on_cancel(self):
        self.parentApp.switchForm("VIEWSHOWS")


# Main menu -------------------------------------------------------

class MakeReservationButton(npyscreen.ButtonPress):
    def whenPressed(self):
        # this is a widget, so don't just call self.parentApp!
        self.parent.parentApp.switchForm("VIEWSHOWS")

class EnterTheaterButton(npyscreen.ButtonPress):
    def whenPressed(self):
        npyscreen.notify_confirm("Entering theater...")

# needed?
class ChangeUserDetails(npyscreen.ButtonPress):
    def whenPressed(self):
        pass
        # do stuff

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
