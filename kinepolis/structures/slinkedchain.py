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
    '''ADT Sorted Linked Chain. It inserts the item at the correct place so that the chain is sorted at all times.'''
    def __init__(self, attribute, head = None, size = 0):
        '''Standard python initializer'''
        self.head = head
        self.size = size
        self._attribute = attribute
        
    def attribute(self):
        '''Returns the attribute or searchkey used in the linked chain.'''
        return self._attribute
        
    def retrieve(self, searchkey):
        '''Looks for an item based on its searchkey in the linked chain. Returns the item if found, else returns None.'''
        current = self.head
        while current != None and searchkey > current.item.__dict__[self._attribute]:
            #Traverse the linked list until the searchkey is found.
            current = current.next
        if current != None and current.item.__dict__[self._attribute] == searchkey:
            return(current.item)
        else:
            return(None)
        
    def isEmpty(self):
        '''If the size of a linked chain is zero, this method will return True.'''
        if self.head == None:
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
            while searchkey > current.next.item.__dict__[self._attribute]:
                #Traverse the linked chain looking for the searchkey.
                current = current.next
            if current.next.item.__dict__[self._attribute] == searchkey:     #If found, the next pointer skips the deleted item.
                print(current.next.item.__dict__[self._attribute])
                current.next = current.next.next
                self.size -= 1
                return(True)
            else:
                return(False)
        
    def insert(self, item):
        '''Basic insert method based on the item. The position will be so that the order of the chain stays intact.'''
        current = self.head
        if current == None:
            #If the list is empty, then the new item is the head.
            self.head = Node(self._attribute, item)
            self.size += 1
            return True
        
        if item.__dict__[self._attribute] < current.item.__dict__[self._attribute]:
            #If the item is smaller than the current head.
            self.head = Node(self._attribute, item)
            self.head.next = current
            self.size += 1
            return True
            
        while current != None:
            if current.next == None:
                tempNode = Node(self._attribute, item)
                current.next = tempNode
                tempNode.next = None
                self.size += 1
                return True
            if current.next.item.__dict__[self._attribute] > item.__dict__[self._attribute]:
                tempNode = Node(self._attribute, item)
                tempNode.next = current.next
                current.next = tempNode
                return True
            current = current.next 
        return False
        
    def inorder(self):
        '''Method to give back all elements of the chain inorder.'''
        current = self.head
        while current != None:
            yield current.item
            current = current.next
    
    def sort(self, attribute, sortFunc = None):
        '''Basic function to sort the chain. If no sortfunction is given the default linkbased bubblesort will be used.'''
        if attribute == self._attribute:
            yield from self.inorder()
            return
        else:
            current = self.head                         #if it doesn't need to be sorted on the searchkey, the chain must be sorted on the different attribute.
            listchain = []
            while current != None:
                listchain.append(current)
                current = current.next
            listchain = sortFunc(listchain, attribute)  #Sort the array.
            for i in listchain:
                yield i
            
    def __str__(self):
        '''Basic chain representation.'''
        if self.head != None:
            return str(self.head)
        else:
            return ('Empty Linked chain')
                    
                        
                
            
    
