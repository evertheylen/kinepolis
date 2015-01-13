
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
        Theater(4, 250),
        Theater(5, 80),
        Theater(6, 90)]:
        
        result.theaters.insert(t)
    
    print('\nTheaters of this cinema:')
    for i in result.theaters.inorder():
        print(i)
    
    # ----- Timeslots -----
    # NOTE Timeslots is simply a python list, the only thing we ever need to do is know 
    # whether it's in it or not. Actually, we never really use it at all. (see Opgave.pdf, no ADT required)
    result.timeslots = [    Timeslot(14,30),
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
        Film(1, "Star Wars: The Force Awakens", 8.1),
        Film(2, "Tron Legacy", 8.9),
        Film(3, "The Avengers", 8),
        Film(4, "The Guardians of the Galaxy", 8.5),
        Film(5, "The Shawshank Redemption", 8.2),
        Film(6, "Transformers 3", 7.5),
        Film(7, "The Godfather", 6.1)]:
        
        result.films.insert(f)
    
    print('\nFilms of this cinema:')
    for f in result.films.inorder():
        print(f)
    
    # ----- Shows -----
    result.shows = createDataStructure("SLinkedChain", "ID")
    #       Show(ID,
    #           date, timeslot, 
    #           theater,
    #           film,
    #           [freeplaces])
    
    result.shows.insert(
        Show(1,
            datetime.date(2015,1,18), result.timeslots[0],
            result.theaters.retrieve(1),
            result.films.retrieve(1),
            ))
    
    result.shows.insert(
        Show(2,
            datetime.date(2015,1,17), result.timeslots[1],
            result.theaters.retrieve(2),
            result.films.retrieve(2),
            ))
    
    result.shows.insert(
        Show(3,
            datetime.date(2015,1,15), result.timeslots[2],
            result.theaters.retrieve(3),
            result.films.retrieve(1),
            ))
    
    result.shows.insert(
        Show(4,
            datetime.date(2015,1,15), result.timeslots[3],
            result.theaters.retrieve(4),
            result.films.retrieve(3),
            ))
    
    result.shows.insert(
        Show(5,
            datetime.date(2015,1,16), result.timeslots[0],
            result.theaters.retrieve(5),
            result.films.retrieve(4),
            ))
    
    result.shows.insert(
        Show(6,
            datetime.date(2015,1,18), result.timeslots[1],
            result.theaters.retrieve(6),
            result.films.retrieve(5),
            ))
    
    result.shows.insert(
        Show(7,
            datetime.date(2015,1,19), result.timeslots[2],
            result.theaters.retrieve(1),
            result.films.retrieve(6),
            ))
    
    result.shows.insert(
        Show(7,
            datetime.date(2015,1,16), result.timeslots[3],
            result.theaters.retrieve(2),
            result.films.retrieve(7),
            ))
    
    print('\nShows of this cinema:')
    for s in result.shows.inorder():
        print(s)
    
    
    # ----- Users -----
    # I've changed the attribute to "mail", because no one ever remembers their own ID...
    result.users = createDataStructure("Hashmap", "mail", toInt=simple_hash)
    for u in [
        # User(ID, firstname, lastname, mail)
        User(1,'Stijn', 'Janssens', 'janssens.stijn@hotmail.com'),
        User(2,'Evert', 'Heylen', 'evert@eestec.be'),
        User(3,'Anthony', 'Hermans', 'anthony@herma.ns'),
        User(4,'Pieter', 'Coeck', 'pieter@coeck.be'),
        User(5,'Dummy', 'Alpha', 'dummy1'),
        User(5,'Dummy', 'Beta', 'dummy2'),
        User(5,'Dummy', 'Gamma', 'dummy3'),
        User(5,'Dummy', 'Delta', 'dummy4'),
        User(5,'Dummy', 'Epsilon', 'dummy5'),
        User(5,'Dummy', 'Zeta', 'dummy6')]:
        
        result.users.insert(u)
    
    print("\nUsers of this cinema")
    for u in result.users.inorder():
        print(u)
    
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