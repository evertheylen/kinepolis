from .base import *

class UnsortedArray(Base):
    def __init__(self, attribute):
        self.array = []
        self._attribute = attribute
    
    def insert(self, el):
        if self._attribute not in el.__dict__.keys():
            print("Wrong type!")
            return None
        
        self.array.append(el)
    
    def retrieve(self, key):
        for el in self.array:
            if el.__dict__[self._attribute] == key:
                return el
        return None
    
    def delete(self, key):
        el = self.retrieve(key)
        if el == None:
            return False
        del(el)
        return True
    
    def inorder(self):
        """ for an UnsortedArray, the naming is wrong.
        """
        
        for el in self.array:
            yield el