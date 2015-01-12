class Reservation:
    """ Class for a reservation """
    
    def __init__(self, ID, user, timeStamp, show, places):
        """ timeStamp is of type datetime.datetime """
        
        self.ID = ID
        self.user = user
        self.timeStamp = timeStamp
        self.show = show
        self.places = places
    
    
    def __str__(self):
        return "Reservation: [{}] by {}, made on {}, {} places for show:\n  {}".format(self.ID, self.user.mail, self.timeStamp, self.places, self.show)
    
    def __repr__(self):
        return self.__str__()

