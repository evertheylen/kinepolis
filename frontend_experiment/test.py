import npyscreen
import traceback

error = None

class User:
    def __init__(self, ID, firstname, lastname, mail):
        """ All string, except ID: int. """
        
        self.ID = ID
        self.firstname = firstname
        self.lastname = lastname
        self.mail = mail
    
    def sendMail(self, message):
        pass
        # send a mail, but not really :)
    
    def __str__(self):
        return "{}:\t{}\t{}\t({})".format(self.ID, self.firstname, self.lastname, self.mail)



# this class is not a form, it's a widget that should be displayed in the form ViewUsersList
class ViewUsers(npyscreen.MultiLineAction):
    def __init__(self, *args, **kwargs):
        super(ViewUsers, self).__init__(*args, **kwargs)
        self.add_handlers({
            "^A": self.when_add_user,
            "^D": self.when_delete_user,
            "^X": self.exit,
            "^P": self.popup
        })
    
    def popup(self, whatever):
        try:
            npyscreen.notify_confirm("test")
        except Exception as e:
            error = e
    
    def display_value(self, vl):
        return str(vl)
    
    def actionHighlighted(self, act_on_this, keypress):
        self.parent.parentApp.getForm('EDITUSER').value = act_on_this.ID
        self.parent.parentApp.switchForm('EDITUSER')
    
    def when_add_user(self, *args, **keywords):
        self.parent.parentApp.getForm('EDITUSER').value = None
        self.parent.parentApp.switchForm('EDITUSER')
    
    def when_delete_user(self, *args, **kwargs):
        self.parent.parentApp.myDatabase.pop(self.values[self.cursor_line].ID)
        self.parent.update_list()
    
    def exit(self, whatever):
        self.parent.parentApp.switchForm(None)


class ViewUsersList(npyscreen.FormMutt):
    MAIN_WIDGET_CLASS = ViewUsers
    def beforeEditing(self):
        self.update_list()
    
    def update_list(self):
        self.wMain.values = list(self.parentApp.myDatabase.values())
        #self.wMain.values = [1, 2, 3]
        self.wMain.display()


class EditUser(npyscreen.ActionForm):
    def create(self):
        self.value = None
        
        self.wgID = self.add(npyscreen.TitleText, name = "ID:")
        self.wgFirstname = self.add(npyscreen.TitleText, name = "Firstname:")
        self.wgLastname = self.add(npyscreen.TitleText, name = "Lastname:")
        self.wgEmail = self.add(npyscreen.TitleText, name = "Email:")
        self.wgPager = self.add(npyscreen.Pager, autowrap=True, values=["test", "lol"])
    
    def beforeEditing(self):
        if self.value: # editing, not creating
            record = self.parentApp.myDatabase[self.value]
            
            self.name = "Record ID: {}".format(record.ID)
            self.record_id = record.ID
            self.wgID.value = record.ID
            self.wgFirstname.value = record.firstname
            self.wgLastname.value = record.lastname
            self.wgEmail.value = record.mail
        else:
            self.name = "New User"
            self.record_id = 0
            self.wgID.value = 0
            self.wgFirstname.value = ""
            self.wgLastname.value = ""
            self.wgEmail.value = ""
    
    def on_ok(self):
        # difference between updating and inserting is not made here
        self.parentApp.myDatabase[int(self.wgID.value)] = User(
            int(self.wgID.value),
            self.wgFirstname.value,
            self.wgLastname.value,
            self.wgEmail.value)
        
        
        self.parentApp.switchFormPrevious()
        
    def on_cancel(self):
        self.parentApp.switchFormPrevious()


class MyApp(npyscreen.NPSAppManaged):
    def __init__(self, database):
        npyscreen.NPSAppManaged.__init__(self)
        self.myDatabase = database
    
    def onStart(self):
        #self.myDatabase = {
            #100: User(100, "Emma", "Stone", "pieterstalktmij@celebmail.com"),
            #101: User(101, "Pieter", "Coeck", "ikstalkemma@sldfj.com"),
            #102: User(102, "Stijn", "Janssens", "sdflkdlkdfj_stijn"),
            #103: User(103, "Anthony", "Hermans", "mailanthony"),
            #}
        
        self.addForm("MAIN", ViewUsersList)
        self.addForm("EDITUSER", EditUser)
 
 
# start MyApp
try:
    db = {
            100: User(100, "Emma", "Stone", "pieterstalktmij@celebmail.com"),
            101: User(101, "Pieter", "Coeck", "ikstalkemma@sldfj.com"),
            102: User(102, "Stijn", "Janssens", "sdflkdlkdfj_stijn"),
            103: User(103, "Anthony", "Hermans", "mailanthony"),
            }
    app = MyApp(db)
    app.run()
    
    print("Emma is now called", db[100].firstname)
    print(error)
except Exception as e:
    traceback.print_exc()
    print(app.myDatabase)
