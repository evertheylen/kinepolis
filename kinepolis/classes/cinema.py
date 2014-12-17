class Cinema:
    '''Class which contains al the other objects, like Theater and Show.'''    
    
    
    def __init__(self, name=None, theaters=None, timeslot=None, show=None, reservations=None, users=None, tickets=None):
        self.name = name
        self.theaters = theaters
        self.timeslots = timeslots
        self.shows = shows
        self.reservations = reservations
        self.users = users
        self.tickets = tickets
        
    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name
