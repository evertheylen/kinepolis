class Reservation:
    """ Klasse voor een reservatie """
    
    def __init__(self, ID, userID, timeStamp, vertoningsID, plaatsen):
        """ timeStamp is van type datetime.datetime """
        
        self.ID = ID
        self.userID = userID
        self.timeStamp = timeStamp
        self.vertoningsID = vertoningsID
        self.plaatsen = plaatsen
    
        # self.tickets wordt manueel aangemaakt op basis van de bovenstaande
        # informatie en het aantal tickets. self.tickets is een tabel.
       
       
    def addTicket(self, ticket):
        pass
        # voeg ticket toe in self.ticket
    
    
    def delTicket(self, ticket):
        pass
        # verwijder ticket in self.ticket