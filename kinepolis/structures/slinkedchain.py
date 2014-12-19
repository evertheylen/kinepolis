import sorting

class Node:
    '''Class Node used in the linked chain.'''
    def __init__(self, attribute, item = None, next = None, precede = None):
        '''Standard python initializer, works with an attribute. This is the searchkey of the object.'''
        self._attribute = attribute
        self.item = item
        self.next = next
        self.precede = precede

    def __str__(self):
        '''Basic visual representation of a node.'''
        if self.item != None:
            output = str(self.item.__dict__[_attribute])
        else:
            return ('Empty node')
        if self.next != None:
            output += ', '+str(self.next)
        return output

class SLinkedChain:
    pass
