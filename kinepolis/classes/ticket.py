class Ticket:
    """ klasse voor een Ticket """
    
    def __init__(self, ID, reservatieID):
        self.ID = ID
        self.reservatieID = reservatieID
        
        # men kan de bijhorende gebruiker bereiken via de bijhorende reservatie.
    