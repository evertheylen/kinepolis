class Vertoning:
    """ Klasse voor een vertoning, bevat een hele hoop eigenschappen
    """
    
    def __init__(self, ID, zaalnummer, datum, tijdslot, vrijeplaatsen, tickets, reservaties):
        self.ID = ID
        self.zaalnummer = zaalnummer
        self.datum = datum  # type datetime.date
        self.tijdslot = tijdslot
        self.vrijeplaatsen = vrijeplaatsen
        self.tickets = tickets  # Stack ? zie onder
        self.reservaties = reservaties  # Queue
    
    
    def kanStarten(self):
        # return True als alle tickets verdeeld zijn
        # return False indien niet
        return True
    
    
    def addTicket(self, ticket):
        """ Mag niet extern gebruikt worden, gebruik eerder addReservatie() """
        self.tickets.insert(ticket)
    
    
    def popTicket(self, ticket):
        # Hier is nog verwarring over (Stack?), ik (Evert) heb een mail gestuurd naar Tom Hofkens hierover.
        self.tickets.delete(ticket)
    
    
    def addReservatie():
        pass
        # als de reservatie geldig is, doorvoeren, anders error.
        
        # gebruik self.addTicket om toe te voegen in de Stack (? zie boven)
        
        # voeg toe in self.reservaties
    
    
    def delReservatie():
        pass
        # Verwijder reservatie uit Stack?
    
    
    def noTickets(self):
        if len(self.tickets) == 0:
            return True
        return False

