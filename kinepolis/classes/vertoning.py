#Auteur: Anthony Hermans
from timeslot import *
from theater import *
#from ticket import *
#from reservation import *

class Show():
    def __init__(self, ID, date=None, theater=None , theatherID=None, timeslot=None,freeplaces = None,tickets = None, reservations = None):
        self.theater = theater
        self.ID = ID
        self.date = date
        self.tijdslot = tijdslot
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

    def getdate(self):
        return self.date

    def setFreePlaces(self):
        self.freeplaces = self.Show.freeplaces

    def getFreePlaces(self):
        return self.freeplaces

    def addTicket(self):
        pass #stack gebruiken

    def popTicket(self):
        pass #stack gebruiken

    def isEmptyTickets(self):
        if self.tickets == 0:
            return True
        else:
            return False

    def addReservatie():
        pass
        # als de reservatie geldig is, doorvoeren, anders error.

        # gebruik self.addTicket om toe te voegen in de Stack (? zie boven)

        # voeg toe in self.reservaties


    def delReservatie():
        pass
        # Verwijder reservatie uit Stack?

    def isEmptyReservations(self):
        if self.Reservations == 0:
            return True
        else:
            return False

