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



class USLinkedChain:
    '''ADT Unsorted Linked Chain. It inserts items at the back and is able to sort itself with different sorting algorithms or with a default linkbased bubble sort.'''
    def __init__(self, attribute, head = None, size = 0):
        '''Standard python initializer'''
        self.head = head
        self.size = size
        self._attribute = attribute
        
    def attribute(self):
        '''Returns the attribute or searchkey used in the linked chain.'''
        return self._attribute
        
    def retrieve(self, searchkey):
        '''Looks for an item based on its searchkey in the linked chain. Returns the item if found else returns None.'''
        current = self.head
        while current != None and searchkey != current.item.__dict__[self._attribute]:
            #Traverse the linked list until the searchkey is found.
            current = current.next
        if current != None:
            return(current.item)
        else:
            return(None) 
        
    def isEmpty(self):
        '''If the size of a linked chain is zero, this method will return True.'''
        if self.size == 0:
            return True
        else:
            return False  
        
    def delete(self, searchkey):
        '''Basic delete function based on the given searchkey.'''
        current = self.head
        if self.head.item.__dict__[self._attribute] == searchkey:
            #Special case: the item to be deleted is the head.
            self.head = self.head.next
            self.size -= 1
            return(True)
        else:
            while searchkey != current.next.item.__dict__[self._attribute]:
                #Traverse the linked chain looking for the searchkey.
                current = current.next
            current.next = current.next.next    #If found, the next pointer skips the deleted item.
            self.size -= 1
            return(True)
        return(False)       # If the searchkey isn't in the list return False
            
    def insert(self, item):
        '''Basic insert method based on the item. NOT ON THE SEARCHKEY!'''
        current = self.head
        if current == None:
            # If the list is empty, then the new item is the head.
            self.head = Node(self._attribute, item)
            self.size += 1
            return True
        while current != None:
            #Else traverse the chain until the end.
            previous = current
            current = current.next
        
        tempnode = Node(self._attribute, item)  #Add the new node at the end of the chain.
        previous.next = tempnode
        current = tempnode
        tempnode.next = None
        self.size += 1
        return True
        
    def ownbubble(self, attribute):
        '''A method to sort the chain with a linkbased bubblesort.'''
        for maxloc in range(self.size, 1, -1):
            current = self.head
            for i in range(maxloc):
                if current != None and current.next != None and current.item.__dict__[attribute] > current.next.item.__dict__[attribute]:
                    current.item, current.next.item = current.next.item, current.item
                if current != None:
                    current = current.next
        
    def inorder(self):
        '''Method to give back all elements of the chain from front to end.'''
        current = self.head
        while current != None:
            yield current.item
            current = current.next
        
    def sort(self, attribute, sortFunc = None):
        '''Basic function to sort the chain. If no sortfunction is given, the default linkbased bubblesort will be used.'''
        if sortFunc == None:
            self.ownbubble(attribute)
        
        else:
            #If not default bubble, create an array of all elements in the chain.
            current = self.head
            listchain = []
            while current != None:
                listchain.append(current)
                current = current.next
            sortFunc(listchain) #Sort the array.
        
        yield from self.inorder()   #Yield all the items.
    
    def __str__(self):
        '''Basic chain representation.'''
        if self.head != None:
            return str(self.head)
        else:
            return ('Empty Linked chain')
        
  
    
    
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
