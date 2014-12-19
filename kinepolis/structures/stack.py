#from .uslinkedchain import USLinkedChain

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return repr(self.data)

class Stack:
    def __init__(self, top = None):
        self.stackTop = top
        self.length = 0
    
    def destroyStack(self):
        self.stackTop.next = None        
        self.stackTop = None
        
    def isEmpty(self):
        if self.stackTop == None:
            return True
        else:
            return False
    
    def push(self, newItem):
        prevtop = self.stackTop
        self.stackTop = Node(newItem)
        self.stackTop.next = prevtop
        if prevtop != None:
            prevtop.prev = self.stackTop
        self.length += 1
        
    def pop(self):
        self.stackTop = self.stackTop.next
        self.length -= 1
        return self.stackTop.data
        
    def getTop(self):
        return self.stackTop.data
        
'''s = Stack()
print(s.isEmpty())
s.push(30)
s.push(40)
s.push(20)
print(s.getTop())
s.pop()
print(s.getTop())
print(s.isEmpty())
s.destroyStack()
print(s.isEmpty())'''
