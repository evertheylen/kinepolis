
class Base:
    """ Base class. Should be extended by another data structure.
    """
    
    def __init__(self, attribute):
        self.array = []
        
        # If you ever manually change this, you are hereby declared the ultimate douchebag ever.
        self._attribute = attribute