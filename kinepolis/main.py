#!/usr/bin/python3

import datetime
import sys
import pickle
import signal

from datastruct import *
from classes import *

from frontend import start_frontend
from backend import start_backend

from example_init import example_cinema

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
        
        print("Cinema to initialize? [kinepolis]")
        name = input("> ")
        if name == '':
            name = "kinepolis"
        
        print(rgbtext("Initializing data[\""+name+"\"]", green))
        
        data[name] = example_cinema(name)
        
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
