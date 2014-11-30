
class UnsortedArray:
    def __init__(self, attribute):
        self.array = []
        self.attribute = attribute
    
    def insert(self, element):
        self.array.append(element)
    
    def retrieve(self, key):
        for el in self.array:
            if el.__dict__[self.attribute] == key:
                return el
        return None
    
    def delete(self, key):
        el = self.retrieve(key)
        if el == None:
            return False
        del(el)
        return True