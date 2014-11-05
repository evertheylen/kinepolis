class Stack:
    def __init__(self):
        self.elements = []
    
    def destroyStack(self):
        del(self)

    def length(self):
        return len(self.elements)

    def isEmpty(self):
        if self.length() == 0:
            return True
        return False

    def push(self, newItem):
        self.elements.append(newItem)
        #print(True)
        return True

    def pop(self):
        if self.isEmpty() == False:
            self.elements.pop()
            return True
        else:
            return False
        
    def getTop(self):
        if self.isEmpty() == False:
            return self.elements[-1]
        else:
            return False
    
    def __str__(self):
        return self.elements
    
stack = Stack()
stack.isEmpty()
stack.push('86')
stack.push('90')
stack.isEmpty()
print(stack.pop())
print(stack.getTop())
print(stack.pop())
print(stack.isEmpty())
print(stack.pop())
print(stack.isEmpty())
