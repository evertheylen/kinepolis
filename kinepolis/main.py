#!/usr/bin/python3

import datetime
import sys
import pickle
import signal

from datastruct import *
from classes import *

from frontend import start_frontend
from backend import start_backend

from etc import *

helptext="""
Created by Anthony Hermans, Pieter Coeck, Stijn Janssens and Evert Heylen.
            
Usage:
<main.py> -h                    print this message
<main.py> [options] [filename]       
Options:
    -b                          open backend for 'filename' (default behaviour is to open frontend)
    --init                      initialize the data in 'filename' (will overwrite!)
    [filename]                  what file to open? (default is 'kinepolis_data')

Example:
    <main.py> -b --init metropolis_data
"""

# global variables
filename = "kinepolis_data"
data = {}


def sigint(signal, frame):
    save()
    sys.exit(1)


def save():
    print('\nSaving...')

    # save data again
    f = open(filename, 'wb+')
    pickle.dump(data, f)
    f.close()

    print(rgbtext('Saving done!',green))


def main():
    # some stuff to make things go smooth...
    signal.signal(signal.SIGINT, sigint)
    global filename
    global data
    
    # set filename if needed
    if len(sys.argv) > 1 and sys.argv[-1][0] != "-":
        # if enough arguments are given, and the last argument is not a flag,
        # change the filename
        filename = sys.argv[-1]
    
    if "-h" in sys.argv:
        print(helptext)
        return
    
    # all data that needs to be saved should go in here
    data = {}
    
    # Initialize variables if needed.
    if "--init" in sys.argv:
        #--- INIT VARS HERE ---------------------------------------------------------------------
        
        data["kinepolis"] = Cinema()
        
        # ----- Theaters -----
        data["kinepolis"].theaters = createDataStructure("RedBlackTree", "ID")
        for t in [
            # Theater(ID, places)
            Theater(1, 10),
            Theater(2, 65),
            Theater(3, 86),
            Theater(4, 250)]:
            
            data["kinepolis"].theaters.insert(t)
        
        print('\nTheaters of this cinema:')
        for i in data["kinepolis"].theaters.inorder():
            print('ID: ',i.ID, '   Number of seats: ', i.places)
        
        # ----- Timeslots -----
        # NOTE Timeslots is simply a python list, the only thing we ever need to do is know 
        # whether it's in it or not. (see Opgave.pdf, no ADT required)
        data["kinepolis"].timeslots = [ Timeslot(14,30),
                                        Timeslot(17,00),
                                        Timeslot(20,00),
                                        Timeslot(22,30) ]
            
        print('\nTimeslots of this cinema:')
        for i in data["kinepolis"].timeslots:
            print(i)
        
        # ----- Films -----
        data["kinepolis"].films = createDataStructure("BinTree", "ID")
        for f in [
            # Film(ID, title, rating)
            Film(1, "Star Wars", 8.1),
            Film(2, "Tron Legacy", 8.9),
            Film(3, "The Avengers", 8),
            Film(4, "The Guardians of the Galaxy", 8.5)]:
            
            data["kinepolis"].films.insert(f)
        
        print('\nFilms of this cinema:')
        for f in data["kinepolis"].films.inorder():
            print(f.title)
        
        # ----- Shows -----
        data["kinepolis"].shows = createDataStructure("SLinkedChain", "ID")
        #       Show(ID,
        #           date, timeslot, 
        #           theater,
        #           film,
        #           [freeplaces])
        
        data["kinepolis"].shows.insert(
            Show(1,
                datetime.date(2014,7,15), Timeslot(20,00),
                data["kinepolis"].theaters.retrieve(3),
                data["kinepolis"].films.retrieve(2),
                ))
        
        data["kinepolis"].shows.insert(
            Show(2,
                datetime.date(2014,7,16), Timeslot(20,00),
                data["kinepolis"].theaters.retrieve(1),
                data["kinepolis"].films.retrieve(4),
                ))
        
        print('\nSecond show of this cinema:  ')
        a = data["kinepolis"].shows.retrieve(2)
        print(a)
        
        
        # ----- Users -----
        # I've changed the attribute to "mail", because no one ever remembers their own ID...
        data["kinepolis"].users = createDataStructure("Hashmap", "mail", toInt=simple_hash)
        for u in [
            # User(ID, firstname, lastname, mail)
            User(1,'Stijn', 'Janssens', 'janssens.stijn@hotmail.com'),
            User(2,'Evert', 'Heylen', 'evert@eestec.be'),
            User(3,'Anthony', 'Hermans', 'anthony@herma.ns'),
            User(4,'Pieter', 'Coeck', 'p@coeck'),
            User(5,'Dummy', 'Tester', 'dum')]:
            
            data["kinepolis"].users.insert(u)        
        
        # ----- Reservations -----
        #   Reservation(ID, 
        #               user,
        #               timeStamp,
        #               show,
        #               places)
        
        data["kinepolis"].addReservation(
            Reservation(1,
                        data["kinepolis"].users.retrieve("p@coeck"),
                        datetime.datetime.now(),
                        data["kinepolis"].shows.retrieve(1),
                        4))
            
        data["kinepolis"].addReservation(
            Reservation(2,
                        data["kinepolis"].users.retrieve("evert@eestec.be"),
                        datetime.datetime.now(),
                        data["kinepolis"].shows.retrieve(2),
                        5))
        
        #--- END OF INIT --------------------------------------------------------------------
        
        # save data
        f = open(filename, 'wb+')
        pickle.dump(data, f)
        f.close()
        
        print("\nSuccesfully initialized the file '%s'."%filename)
    
    
    # load data
    try:
        f = open(filename, "rb")
        data = pickle.load(f)
    except:
        print(rgbtext("Error while trying to open the file '%s', perhaps you have to initialize it first (--init)?"%filename))
        return
    f.close()
    
    
    if "-b" in sys.argv:
        start_backend(data, save)
    else:
        start_frontend(data)
    
    
    # save data again
    save()


if __name__=="__main__":
    main()
