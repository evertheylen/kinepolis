# Auteur: Anthony Hermans

from .timeslot import *
from .theater import *
from .ticket import *
from .reservation import *

class Show():
    def __init__(self, ID, date=None, theater=None , theatherID=None, timeslot=None,freeplaces = None,tickets = None, reservations = None):
        self.theater = theater
        self.ID = ID
        self.date = date
        self.timeslot = timeslot
        self.freeplaces = freeplaces
        self.theaterID = theater
        self.tickets = tickets
        self.reservations = reservations

    def setTheater(self, ID):
        self.theater = Theater()
        self.theater.getID(ID)

    def getTheater(self):
        return self.theater

    def setTimeslot(self, timeslot):
        self.timeslot = Slot(timeslot)

    def getTimeslot(self):
        return self.timeslot

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setFreePlaces(self):
        self.freeplaces = self.Show.freeplaces

    def getFreePlaces(self):
        return self.freeplaces

    def addTicket(self):
        pass # TODO stack gebruiken

    def popTicket(self):
        pass #stack gebruiken

    def isEmptyTickets(self):
        if self.tickets.isEmpty():
            return True
        else:
            return False

    def addReservatie():
        pass
        # if the reservation is valid, add it, otherwise error.

        # use self.addTicket to add tickets to stack??? TODO


    def delReservatie():
        pass
        # Delete reservation from Stack?
        # TODO Good question
    

    def isEmptyReservations(self):
        if self.reservations.isEmpty():
            return True
        else:
            return False

