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