import datetime

    #""" Class for a timeslot.
    #Subclass of datetime.time, initialize with:

    #Timeslot(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

    #"""

    # default __str__() will return something like
    #  12:34

class Timeslot(datetime.time):
    def __str__(self):
        return ("{:%H:%M}".format(self))
