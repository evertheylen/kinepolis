# Auteur: Anthony Hermans

from structures.stack import Stack
from structures.queue import Queue

from .ticket import Ticket

import datetime

class Show:
    def __init__(self, ID, date, timeslot, theater, film, freeplaces=-1, tickets = None):
        self.ID = ID
        self.date = date
        self.timeslot = timeslot
        self.fulldate = datetime.datetime(date.year, date.month, date.day, timeslot.hour, timeslot.minute)
        self.theater = theater
        self.film = film
        if freeplaces == -1:
            freeplaces = theater.places
        self.freeplaces = freeplaces
        # this number is managed by the 'parent' cinema
        
        if tickets==None:
            tickets = Stack()
        self.tickets = tickets
            

    # Tickets -----------------------------

    def pushTicket(self, ticket):
        #print("pushing ticket")
        return self.tickets.push(ticket)

    def popTicket(self):
        return self.tickets.pop()

    def isEmptyTickets(self):
        return self.tickets.isEmpty()

    
    
    # UI ----------------------------------
    
    def __str__(self):
        return "Show: [{0}] {1}, {2}\t in theater {3}\t playing {4: <35} {5} places left.\t({6} tickets)".format(
                self.ID, str(self.date), str(self.timeslot), str(self.theater.ID), "'"+str(self.film.title)+"'",
                str(self.freeplaces), self.tickets.length)
    
    def __repr__(self):
        return self.__str__()
