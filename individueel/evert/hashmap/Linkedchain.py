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
        
    # Modified 'node' --> 'key'
    def remove(self, key):
        current = self.head
        previous = None
        while current != None:
            if current.item.searchkey() == key:
                # 'Delete' the element
                if previous!=None:
                    previous.next = current.next
                else:
                    # previous was None, alter head
                    self.head = current.next
                return current
            previous = current
            current = current.next
        
        return None # Didn't find it...
                    
                
    
    # Modified this function so that it automatically creates a new node
    def insert(self, newitem, node1 = None, node2 = None):
        newnode = Node(newitem)
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
    
    # Modification by Evert Heylen
    def retrieve(self, key):
        current = self.head
        while current != None:
            if current.item.searchkey() == key:
                return current.item
            current = current.next
        
        return None # Didn't find it...
    
    def __str__(self):
        s = ""
        if self.head != None:
            current = self.head
            s += "["
            while current != None:
                s += str(current.item) + ", "
                current = current.next
            s += "]\n"
            return s
        else:
            return 'Empty Linked chain'
    def __repr__(self):
        return self.__str__()

# DO NOT USE :)
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
        if current == None:
            return None # didn't find it.
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
    

