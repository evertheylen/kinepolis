from structures.queue import Queue
from .ticket import Ticket

class Cinema:
    def __init__(self, name="defaultname", theaters=None, timeslots=None, shows=None, films=None, users=None, reservations=None, autoExecute=True):
        self.name = name
        self.theaters = theaters
        self.timeslots = timeslots
        self.shows = shows
        self.films = films
        if reservations == None:
            reservations = Queue()
        self.reservations = reservations
        self.reservationCounter = 0
        self.users = users
        
        self.autoExecute = autoExecute
        
    # Reservations ------------------------
    
    # add a reservation to the reservations queue.
    def addReservation(self, reservation):
        if reservation.places > reservation.show.freeplaces:
            #print('Er is te weinig plaats in de zaal voor uw reservatie. Deze zal niet kunnen worden afgewerkt.')
            return False
        else:
            self.reservations.enqueue(reservation)
            if self.autoExecute: # automatically call executeReservations if set to True (default)
                self.executeReservations(1)
            reservation.show.freeplaces -= reservation.places
            self.reservationCounter += 1  # to determine a unique ID in the frontend
            return True
    
    def isEmptyReservations(self):
        return self.reservations.isEmpty()
    
    # 'transport' reservations to tickets Stack
    def executeReservations(self, count=-1):
        # when this function gets called, we should be sure that there are enough free places
        i = 1
        # count of -1 means we execute all reservations possible.
        while True:
            reservation = self.reservations.dequeue()
            
            if reservation == None:
                break;
            
            for i in range(reservation.places):
                #print("should push")
                reservation.show.pushTicket(Ticket())

            if (count != -1 and i>=count):
                # Break if we are about to exceed the count, or if there are no more reservations left
                break