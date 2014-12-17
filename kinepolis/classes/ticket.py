class Ticket:
    def __init__(self, ID=None, ReservationID=None):
        self.ID = ID
        self.ReservationID = ReservationID
        
    def getReservationID(self):
        return ReservationID
    
    def setReservationID(self, ReservationID):
        self.ReservationID = ReservationID
