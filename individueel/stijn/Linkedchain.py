class Node:
    def __init__(self, item = None, next = None, precede = None):
        self.item = item
        self.next = next
        self.precede = precede
    def __str__(self):
        if self.item != None:
            output = str(self.item)
        else:
            return ('Empty node')
        if self.next != None:
            output += ', '+str(self.next)
        return output
        
        

class Linkedchain:
    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = size
        
    def remove(self, node):
        current = self.head
        if self.head == node:
            self.head = self.head.next
            return(current)
        else:
            while node != current.next:
                current = current.next
            current.next = node.next
            return(current)
            
    def insert(self, newnode, node1 = None, node2 = None):
        if node1 == None:
            newnode.next = self.head
            self.head = newnode
        elif node2 == None:
            node1.next = newnode
            newnode.next = None
        else:
            node1.next = newnode
            newnode.next = node2
        self.size += 1           
    
    def __str__(self):
        if self.head != None:
            return str(self.head)
        else:
            return ('Empty Linked chain')

            
class DoublyLinkedchain(Linkedchain):
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
            newnode.next.precede = newnode
    

