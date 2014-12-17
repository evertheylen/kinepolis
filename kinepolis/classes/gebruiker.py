class Gebruiker:
    """ Klasse voor een gebruiker """
    
    def __init__(self, ID, voornaam, achternaam, email):
        """ Allemaal string, buiten ID: int. """
        
        self.ID = ID
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.email = email
    
    def sendMail(self, message):
        pass
        # stuur zogezegd een mail naar de gebruiker