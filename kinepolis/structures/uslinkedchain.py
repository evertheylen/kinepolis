import sorting

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

class USLinkedChain:
    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = size
        self._attribute = attribute
        
    def attribute(self):
        return self._attribute
        
    def retrieve(self, searchkey):
        current = self.head
        while searchkey != current.item.__dict__[_attribute]:
            current = current.next
        return(current.item)      
        
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False  
        
    def delete(self, searchkey):
        current = self.head
        if self.head.item.__dict__[_attribute] == searchkey:
            self.head = self.head.next
            return(True)
        else:
            while searchkey != current.next.item.__dict__[_attribute]:
                current = current.next
            current.next = current.next.next
            return(True)
        return(False)
            
    def insert(self, searchkey):
        current = self.head
        if current == None:
            self.head = Node(_attribute, searchkey)
            self.size += 1
            return True
        while current != None:
            previous = current
            current = current.next
        
        tempnode = Node(_attribute, searchkey)
        previous.next = tempnode
        current = tempnode
        tempnode.next = None
        self.size += 1
        return True
        
    def sort(self, attribute, sortFunc = ownbubble):
        # TODO linkedchain: 
        current = self.head
        listchain = []
        while current != None:
            listchain.append(current)
            current = current.next
        sortFunc(listchain)
        
        yield from self.inorder()
    
    def inorder(self):
        current = self.head
        while current != None:
            yield current
            current = current.next
    
    def __str__(self):
        if self.head != None:
            return str(self.head)
        else:
            return ('Empty Linked chain')
        
def ownbubble():
    pass    
    
    
'''class DoublyLinkedchain(Linkedchain):
    def __init__(self):
        Linkedchain.__init__(self)
        self.precede(self.head)
        
    def precede(self, current = None, previous = None):
        if current != None:
            if current != self.head and previous != None:
                current.precede = previous
                self.precede(current.next, current)
            else:
                self.precede(current.next, current)
        else:
            return
                
    def remove(self, node):
        i = self.head
        current = Linkedchain.remove(self,node)
        while i != current.precede:
            i = i.next
        current.next.precede = i
        
    def insert(self, newnode, node1 = None, node2 = None):
        Linkedchain.insert(self, newnode, node1, node2)
        i = self.head
        if i == newnode:
            newnode.precede = None
        else:
            while i.next != newnode:
                i.next = i.next.next
            newnode.precede = i
        if newnode.next != None:
            newnode.next.precede = newnode'''
