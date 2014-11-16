import datetime

class Tijdslot(datetime.time):
    pass
    """ Klasse voor een tijdslot. 
    Subklasse van datetime.time, initializeren met:
    
    Tijdslot(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
    
    """
    
    # default __str__() will return something like
    #  12:34:56