import datetime


    #""" Klasse voor een tijdslot. 
    #Subklasse van datetime.time, initializeren met:
    
    #Tijdslot(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
    
    #"""
    
    # default __str__() will return something like
    #  12:34:56
#Auteur: Anthony Hermans

class Slot(datetime.time):
    def __init__(self, timeslot=None):
        self.timeslot = timeslot
        if timeslot == "13.30u":
            print("The timeslot " + timeslot + " is available.")
            return
        if timeslot == "17.00u":
            print("The timeslot " + timeslot + " is available.")
            return
        if timeslot == "20.00u":
            print("The timeslot " + timeslot + " is available.")
            return
        if timeslot == "22.30u":
            print("The timeslot " + timeslot + " is available.")
            return
        else:
            print("The timeslot " + timeslot +  " is not available.")
            return
