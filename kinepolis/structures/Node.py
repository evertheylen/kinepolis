class Node:
    def __init__(self, attribute, item = None, next = None, precede = None):
        self._attribute = attribute
        self.item = item
        self.next = next
        self.precede = precede

    def __str__(self):
        if self.item != None:
            output = str(self.item.__dict__[_attribute])
        else:
            return ('Empty node')
        if self.next != None:
            output += ', '+str(self.next)
        return output
        
        

