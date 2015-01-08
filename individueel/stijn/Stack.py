import Node
import Linkedchain

class Stack():
    def __init__(self, top = None):
        self.linkedchain = Linkedchain.Linkedchain(top)
        
    def destroyStack(self):
        self.linkedchain.head = None
        
    def isEmpty(self):
        if self.linkedchain.head == None:
            return True
        else:
            return False
        
    def push(self, newItem):
        self.linkedchain.insert(newItem)
    
    def pop(self):
        stackTop = self.linkedchain.head
        if stackTop != None:
            self.linkedchain.remove(self.linkedchain.head)
            stackTop.next = None
        return stackTop
        
    def getTop(self):
        stackTop = self.linkedchain.head
        if stackTop != None:
            stackTop.next = None
        return stackTop
        
    def __str__(self):
        return str(self.linkedchain)
        
