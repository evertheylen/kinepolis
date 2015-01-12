
import datetime

from datastruct import *
from classes import *

from etc import *

def example_cinema(name):
    #--- INIT VARS HERE ---------------------------------------------------------------------
    
    result = Cinema()
    result.name = name
    
    # ----- Theaters -----
    result.theaters = createDataStructure("RedBlackTree", "ID")
    for t in [
        # Theater(ID, places)
        Theater(1, 10),
        Theater(2, 65),
        Theater(3, 86),
        Theater(4, 250)]:
        
        result.theaters.insert(t)
    
    print('\nTheaters of this cinema:')
    for i in result.theaters.inorder():
        print('ID: ',i.ID, '   Number of seats: ', i.places)
    
    # ----- Timeslots -----
    # NOTE Timeslots is simply a python list, the only thing we ever need to do is know 
    # whether it's in it or not. (see Opgave.pdf, no ADT required)
    result.timeslots = [ Timeslot(14,30),
                                    Timeslot(17,00),
                                    Timeslot(20,00),
                                    Timeslot(22,30) ]
        
    print('\nTimeslots of this cinema:')
    for i in result.timeslots:
        print(i)
    
    # ----- Films -----
    result.films = createDataStructure("BinTree", "ID")
    for f in [
        # Film(ID, title, rating)
        Film(1, "Star Wars", 8.1),
        Film(2, "Tron Legacy", 8.9),
        Film(3, "The Avengers", 8),
        Film(4, "The Guardians of the Galaxy", 8.5)]:
        
        result.films.insert(f)
    
    print('\nFilms of this cinema:')
    for f in result.films.inorder():
        print(f.title)
    
    # ----- Shows -----
    result.shows = createDataStructure("SLinkedChain", "ID")
    #       Show(ID,
    #           date, timeslot, 
    #           theater,
    #           film,
    #           [freeplaces])
    
    result.shows.insert(
        Show(1,
            datetime.date(2014,7,15), Timeslot(20,00),
            result.theaters.retrieve(3),
            result.films.retrieve(2),
            ))
    
    result.shows.insert(
        Show(2,
            datetime.date(2014,7,16), Timeslot(20,00),
            result.theaters.retrieve(1),
            result.films.retrieve(4),
            ))
    
    print('\nSecond show of this cinema:  ')
    a = result.shows.retrieve(1)
    print(a)
    
    
    # ----- Users -----
    # I've changed the attribute to "mail", because no one ever remembers their own ID...
    result.users = createDataStructure("Hashmap", "mail", toInt=simple_hash)
    for u in [
        # User(ID, firstname, lastname, mail)
        User(1,'Stijn', 'Janssens', 'janssens.stijn@hotmail.com'),
        User(2,'Evert', 'Heylen', 'evert@eestec.be'),
        User(3,'Anthony', 'Hermans', 'anthony@herma.ns'),
        User(4,'Pieter', 'Coeck', 'p@coeck'),
        User(5,'Dummy', 'Tester', 'dum')]:
        
        result.users.insert(u)        
    
    # ----- Reservations -----
    #   Reservation(ID, 
    #               user,
    #               timeStamp,
    #               show,
    #               places)
    
    """
    result.addReservation(
        Reservation(1,
                    result.users.retrieve("p@coeck"),
                    datetime.datetime.now(),
                    result.shows.retrieve(1),
                    4))
        
    result.addReservation(
        Reservation(2,
                    result.users.retrieve("evert@eestec.be"),
                    datetime.datetime.now(),
                    result.shows.retrieve(2),
                    5))
    """
    
    #--- END OF INIT --------------------------------------------------------------------
    
    return result