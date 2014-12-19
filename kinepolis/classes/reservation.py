class Reservation:
    """ Class for a reservation """
    
    def __init__(self, ID, user, timeStamp, show, places):
        """ timeStamp is of type datetime.datetime """
        
        self.ID = ID
        self.user = user
        self.timeStamp = timeStamp
        self.show = show
        self.places = places
    
       
       
    def getID(self):
        return self.ID
    
    def getUser(self):
        return self.user
    
    def getTimeStamp(self):
        return self.timeStamp
    
    def getShow(self):
        return self.show
    
    def getPlaces(self):
        return self.places
    
    def setUser(self, user):
        self.user = user
    
    def setTimeStamp(self, ts):
        self.timeStamp = ts
    
    def setShow(self, show):
        self.show = show
    
    def setPlaces(self, pl):
        self.places = pl
