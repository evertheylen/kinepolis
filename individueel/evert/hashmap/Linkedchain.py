
# Modified version of the Linkedchain, originally made by Stijn.
# Modified by Evert Heylen, as an example for the hash table.

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
        return True
    
    # Modified
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
    
    def inorder(self):
        current = self.head
        while current != None:
            yield current.item
            current = current.next

    

