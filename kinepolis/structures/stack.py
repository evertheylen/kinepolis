from .uslinkedchain import USLinkedChain

class Stack:
    def __init__(self, attribute, top = None):
        self._attribute = attribute
        self.linkedchain = USLinkedChain(attribute, top)
        self.stackTop = top
    
    def attribute(self):
        return self._attribute
    
    def destroyStack(self):
        self.linkedchain.head = None
        
    def isEmpty(self):
        if self.linkedchain.head == None:
            return True
        else:
            return False
    
    def push(self, newItem):
        self.linkedchain.insert(newItem, 'push')
        self.stackTop = self.linkedchain.head
        
    def pop(self):
        self.linkedchain.delete(self.linkedchain.head.item.__dict__[self._attribute])
        self.stackTop = self.linkedchain.head
        return self.stackTop.item
        
    def getTop(self):
        return self.stackTop.item
