class Cinema:
    """ Klasse die al de andere objecten bevat, zoals Zaal en Vertoning. """
    
    def __init__(self, naam, zalen, tijdslots, vertoningen, reservaties, gebruikers, tickets):
        self.naam = naam
        self.zalen = zalen
        self.tijdslots = tijdslots
        self.vertoningen = vertoningen
        self.reservaties = reservaties
        self.gebruikers = gebruikers
        self.tickets = tickets
    
    