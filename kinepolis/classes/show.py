# Auteur: Anthony Hermans

from structures.stack import Stack
from structures.queue import Queue

from .ticket import Ticket

class Show:
    def __init__(self, ID, date, timeslot, theater, film, freeplaces=-1, tickets = Stack()):
        self.ID = ID
        self.date = date
        self.timeslot = timeslot
        self.theater = theater
        self.film = film
        if freeplaces == -1:
            freeplaces = theater.places
        self.freeplaces = freeplaces
        
        self.tickets = tickets
        

    def setTheater(self, theater):
        self.theater = theater
        
    def getfilmID(self):
        return self.film.ID

    def getTheater(self):
        return self.theater

    def setTimeslot(self, timeslot):
        self.timeslot = timeslot

    def getTimeslot(self):
        return self.timeslot

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setFreePlaces(self, freeplaces):
        self.freeplaces = freeplaces

    def getFreePlaces(self):
        return self.freeplaces
            

    # Tickets -----------------------------

    def pushTicket(self, ticket):
        return self.tickets.push(ticket)

    def popTicket(self):
        return self.tickets.pop()

    def isEmptyTickets(self):
        return self.tickets.isEmpty()

