def sortingbubblesort(a, b):
    return a


class Node():
    def __init__(self, attribute, values=[None, None, None], parent=None, children=[None, None, None, None]):
        '''Makes an object of the class Node'''
        self._attribute = attribute
        self.values = values
        self.parent = parent
        self.children = children

    def __repr__(self):
        '''Operator overloading for the visual representation of a Node when it gets printed.'''
        output = []
        if self.values[0] != None:
            output.append(self.values[0])
        if len(self.values) > 1 and self.values[1] != None:
            output.append(self.values[1])
        if len(self.values) > 1 and self.values[2] != None:
            output.append(self.values[2])
        if self.parent != None:
            output.append("parent:values")
            if self.parent.values[0] != None:
                output.append(self.parent.values[0])
            if self.parent.values[1] != None:
                output.append(self.parent.values[1])
            if self.parent.values[2] != None:
                output.append(self.parent.values[2])
            if self.parent.parent != None:
                output.append(self.parent.parent)
        if len(self.children) > 0 and self.children[0] != None:
            output.append("left child")
            output.append(self.children[0])
        if len(self.children) > 1 and self.children[1] != None:
            output.append("mid child:")
            output.append(self.children[1])
        if len(self.children) > 2 and self.children[2] != None:
            output.append("right child:")
            output.append(self.children[2])
        return str(output)

    def attribute(self):
        return self._attribute


    def _key(self, el):
        return el.__dict__[self._attribute]


    def searchkey(self):
        '''Return the searchkey of an item. This is the attribute of the item that is defined as the searchkey'''
        if self.values[0] == None and self.values[1] == None and self.values[2] == None:
            return None
        else:
            return self.values[:3].__dict__[self.attribute]

    def isLeaf(self):
        '''Determines is self is a leafNode'''
        if self.children[0] == None and self.children[1] == None and self.children[2] == None and self.children[3] == None:
            return True
        else:
            return False

    def split(self):
        '''Splits the node if necessary'''
        if self.parent == None:         #Self is root
            self.children[0] = Node(self._attribute, [self.values[0],None,None], self, [self.children[0], None, self.children[1], None])  #Linkerkind
            self.children[1] = Node(self._attribute, [None,None,None], self, [None,None, None, None])                                     #Middenste kind
            self.children[2] = Node(self._attribute, [self.values[2],None,None], self, [self.children[2], None, self.children[3], None])  #Rechterkind
            self.children[3] = Node(self._attribute, [None,None,None], self, [None,None, None, None])                                     #4de Kind, handig voor insert
            self.values[0] = None       #self behoudt enkel de middenste value
            self.values[2] = None
            return
        else:                           #Self is geen root
            if self.parent.values[0] == None and self.parent.values[1] == None:                      #Parent node is niet vol
                if self.values[0] != None and self.values[1] != None and self.values[2] != None:    #Self node is vol
                    if self._key(self.values[1]) <= self._key(self.parent.values[1]):                                     #De middenste value is kleiner dan middenste value van de parent
                        self.parent.values[0] = self.values[1]                                      #Eerste value van parent is gelijk aan middenste value van self
                        self.parent.children[1].insert(self.values[2])                   #Derde value van self wordt in middenste kind geplaatst
                        self.values[2] = None                                                       #Overige waarden van self worden terug op None gezet
                        self.values[1] = None
                        return
                    if self._key(self.values[1]) > self._key(self.parent.values[1]):                                      #De middenste value van self is groter dan de value in parent
                        self.parent.values[0] = self.parent.values[1]                               #De values in parent worden terug gerangschikt
                        self.parent.values[1] = self.values[1]
                        self.parent.children[1].insert(self.values[0])                   #De eerste value van rechterkind worden in het middenste kind geplaatst
                        self.values[0] = None                                                       #Overige waarden van self worden terug op None gezet
                        self.values[1] = None
                        return
            else:                                                                                   #De parent bevat nu 3 waarden
                if self.parent.values[0] == None and self.parent.values[1] == None:                  #De parent is niet vol
                    if self._key(self.values[1]) <= self._key(self.parent.values[0]):                                     #Als de middenste value van self is kleiner dan de parent value
                        temp = self.parent.values[0]                                                #De values van de parent worden gerangschikt
                        self.parent.values[2] = self.parent.values[1]
                        self.parent.values[1] = temp
                        self.parent.values[0] = self.values[1]                                      #Mid value wordt in de parent geplaatst
                        self.values[1] = None                                                       #Mid value is nu terug None
                        return
                    elif self._key(self.values[1]) > self._key(self.parent.values[0])\
                        and self._key(self.values[1]) <= self._key(self.parent.values[1]):    #self is het middenste kind en de mid value wordt de mid value van de parent

                        self.parent.values[2] = self.parent.values[1]
                        self.parent.values[1] = self.values[1]
                        self.values[1] = None
                        return
                    elif self._key(self.values[1]) > self._key(self.parent.values[1]):                                    #Self is het rechterkind
                        self.parent.values[2] = self.values[1]
                        self.values[1] = None
                        return
                if self.parent.values[2] == None and self.parent.values[0] != None and self.parent.values[1] != None:   #Parent heeft 2 values
                    if self._key(self.values[1]) < self._key(self.parent.values[0]):          #self is het linkerkind
                        self.parent.values[2] = self.parent.values[1]
                        self.parent.values[1] = self.parent.values[0]
                        self.parent.values[0] = self.values[1]
                        self.values[1] = None
                        self.parent.children[3] = self.parent.children[2]
                        self.parent.children[2] = self.parent.children[1]
                        self.parent.children[0] = Node(self._attribute, [self.values[0],None,None], self.parent, [self.children[0], None, self.children[1], None])
                        self.parent.children[1] = Node(self._attribute, [self.values[2],None,None], self.parent, [self.children[2], None, self.children[3], None])
                        self.parent.split()                #Parent wordt gesplitst want bevat 3 waarden
                        return
                    if self._key(self.values[1]) > self._key(self.parent.values[0])\
                        and self._key(self.values[1]) <= self._key(self.parent.values[1]):   #self is het middenste kind

                        self.parent.values[2] = self.parent.values[1]
                        self.parent.values[1] = self.values[1]
                        self.values[1] = None
                        self.parent.children[3] = self.parent.children[2]
                        self.parent.children[2] = Node(self._attribute, [self.values[2],None,None], self.parent, [self.children[2], None, self.children[3], None])
                        self.parent.children[1] = Node(self._attribute, [self.values[0],None,None], self.parent, [self.children[0], None, self.children[1], None])
                        self.parent.children[0] = self.parent.children[0]
                        self.parent.split()                #Parent wordt gesplitst want bevat 3 waarden
                        return
                    if self._key(self.values[1]) > self._key(self.parent.values[1]):      #self is het rechterkind
                        self.parent.values[2] = self.values[1]
                        self.values[1] = None
                        self.parent.children[3] = Node(self._attribute, [self.values[2],None,None], self.parent, [self.children[2], None, self.children[3], None])
                        self.parent.children[2] = Node(self._attribute, [self.values[0],None,None], self.parent, [self.children[0], None, self.children[1], None])
                        self.parent.children[1] = self.parent.children[1]
                        self.parent.children[0] = self.parent.children[0]
                        self.parent.split()               #Parent wordt gesplitst want bevat 3 waarden
                        return



    def insert(self, NewItem):
        '''Inserts a value in the TwoThreeTreeNode'''
        if self.children[0] == None and self.children[1] == None and self.children[2] == None and self.children[3] == None:     #isLeaf methode uit cursus
            if self.values[0] == None or self.values[1] == None or self.values[2] == None:
                if self.values[0] == None:
                    if self.values[2] == None:
                        self.values[0] = NewItem
                        return
                    else:
                        if self._key(self.values[2]) <= self._key(NewItem):
                            temp = self.values[2]
                            self.values[2] = NewItem
                            self.values[0] = temp
                            return
                        else:
                            self.values[0] = NewItem
                            return
                if self.values[1] == None:
                    if self.values[2] == None:
                        if self._key(self.values[0]) <= self._key(NewItem):
                            self.values[1] = NewItem
                            return
                        else:
                            temp = self.values[0]
                            self.values[0] = NewItem
                            self.values[1] = temp
                            return
                    else:
                        if self._key(NewItem) >= self._key(self.values[0]):
                            if self._key(self.values[2]) <= self._key(NewItem):
                                temp = self.values[2]
                                self.values[2] = NewItem
                                self.values[1] = temp
                                if self.values[0] != None and self.values[1] != None and self.values[2] != None:
                                    self.split()
                                return
                            else:
                                self.values[1] = NewItem
                                return
                        else:
                            temp = self.values[0]
                            self.values[0] = NewItem
                            self.values[1] = temp
                            return
                if self.values[2] == None:
                    if self._key(self.values[1]) <= self._key(NewItem):
                        self.values[2] = NewItem
                        self.split()
                        return
                    else:
                        if self._key(self.values[1]) >= self._key(NewItem):
                            temp = self.values[1]
                            self.values[1] = NewItem
                            self.values[2] = temp

                            if self._key(self.values[0]) >= self._key(self.values[1]):
                                temp = self.values[0]
                                self.values[0] = self.values[1]
                                self.values[1] = temp
                        self.split()
                        return
        else:           #Het bevat kinderen
            if self.values[0] == None:
                if self._key(NewItem) <= self._key(self.values[1]):
                    self.children[0].insert(NewItem)
                if self._key(NewItem) > self._key(self.values[1]):
                    self.children[2].insert(NewItem)
            else:
                if self._key(NewItem) < self._key(self.values[0]):
                    self.children[0].insert(NewItem)
                    return
                if self._key(NewItem) <= self._key(self.values[1]) and self._key(NewItem) >= self._key(self.values[0]):
                    self.children[1].insert(NewItem)
                    return
                if self._key(NewItem) > self._key(self.values[1]):
                    self.children[2].insert(NewItem)
                    return

    def fix(self):
        '''Fixes the node if necessary'''
        if self.parent == None:         #Self is de wortel
            del self                    #Delete de wortel

        else:
            if self == self.parent.children[0]: #Herverdeling linkerkind
                if parent.children[1] != None and self.parent.children[1].values[0] != None and self.parent.children[1].values[1] != None:
                    temp = self.parent.values[0]
                    self.parent.values[0] = self.parent.children[1].values[0]
                    self.parent.children[1].values[0] = None
                    self.values[1] = temp
                if parent.children[2] != None and self.parent.children[2].values[0] != None and self.parent.children[2].values[1] != None:
                    temp = self.parent.values[0]
                    self.parent.values[0] = self.parent.children[2].values[0]
                    self.parent.children[1].values[0] = None
                    self.values[1] = temp

            if self == self.parent.children[1]: #Herverdeling middenste kind
                if parent.children[0] != None and self.parent.children[0].values[0] != None and self.parent.children[0].values[1] != None:
                    temp = self.parent.values[1]
                    self.parent.values[0] = self.parent.children[0].values[1]
                    self.parent.children[0].values[1] = None
                    self.values[1] = temp
                elif self.parent.children[2] != None and self.parent.children[2].values[0] != None and self.parent.children[2].values[1] != None:
                    temp = self.parent.values[0]
                    self.parent.values[1] = self.parent.children[2].values[0]
                    self.parent.children[2].values[0] = None
                    self.values[1] = temp

            if self == self.parent.children[2]: #Herverdeling rechterkind
                if parent.children[1] != None and self.parent.children[1].values[0] != None and self.parent.children[1].values[1] != None:
                    temp = self.parent.values[0]
                    self.parent.values[0] = self.parent.children[1].values[1]
                    self.parent.children[1].values[1] = None
                    self.values[1] = temp
                if parent.children[0] != None and self.parent.children[0].values[0] != None and self.parent.children[0].values[1] != None:
                    temp = self.parent.values[0]
                    self.parent.values[0] = self.parent.children[1].values[1]
                    self.parent.children[0].values[1] = None
                    self.values[1] = temp

            if self.children[0] != None or self.children[1] != None or self.children[2] != None: #self is interne knoop
                #Verplaats het juiste kind van sibling naar self
                if self == self.parent.children[0]:
                    self = self.parent.children[2].children[0]
                    return
                elif self == self.parent.children[1] and self.parent.children[1] != None:
                    self = self.parent.children[2].children[0]
                    return
                elif self == self.parent.children[2]:
                    if self.parent.children[1] != None:
                        self = self.parent.children[1]
                    else:
                        self = self.parent.children[0]
            else:       #Samenvoegen van knopen

                if self.children[0] != None or self.children[1] != None or self.children[2] != None: #self is interne knoop
                    if self == self.parent.children[0]:
                        self.parent.children[2].children[0] = self
                        return
                    elif self == self.parent.children[1] and self.parent.children[1] != None:
                        self.parent.children[2].children[0] = self
                        return
                    elif self == self.parent.children[2]:
                        if self.parent.children[1] != None:
                            self.parent.children[1] = self
                        else:
                            self.parent.children[0] = self
                del self
                if self.parent == None:
                    self.parent.fix(self._attribute)

    def delete(self, key):
        '''Delete a the specific key from the tree'''
        if key == self._key(self.values[0]) or key == self._key(self.values[1]):
            print("Node is gevonden")
            if self.children[0] != None or self.children[1] != None or self.children[2] != None or self.children[3] != None: #Node is geen blad
                print("Node is geen blad")
                self.inorderSuccessor() # wtf
            if self._key(self.values[0]) == key:
                self.values[0] = self.values[1]
                self.values[1] = None
            if self._key(self.values[1]) == key:
                self.values[1] = None
            if self.values[0] == None and self.values[1] == None:   #leafNode heeft geen items
                self.fix(attribute)                                 #fix self
                success = True
                return success
        elif key <= self._key(self.values[1]) and self.children[0] != None:
            self.children[0].delete(key)
            return
        elif self.values[1] != None and self.values[0] != None:
            if key < self._key(self.values[0]) and self.children[0] != None:
                self.children[0].delete(key)
                return
            if key > self._key(self.values[0]) and key < self._key(self.values[1]) and self.children[1] != None:
                self.children[1].delete(key)
                return
            if key > self._key(self.values[1]) and self.children[2] != None:
                self.children[2].delete(key)
                return
        else:
            success = False
            return success

    def inorderSuccessor(self):
        if self.children[0] == None and self.children[1] == None and self.children[2] == None and self.children[3] == None: #Node is een blad
            if self.values[1] != None:
                self.values[0] = self.values[1]
                self.values[1] = None
                return
            if self.parent.values[0] != None:
                temp = self.parent.values[0]
                self.parent.values[0] = None
                self.values[0] = temp
                return
        elif self.children[2] != None:
            self.children[2].inorderSuccessor() # wtf
        elif self.values[1] != None:
            self.children[1].inorderSuccessor() # wtf

    def retrieve(self, Searchkey):
        '''Search the specific Searchkey in the tree, return True if Searchkey is found, otherwise return False'''
        if Searchkey == self._key(self.values[0]) or Searchkey == self._key(self.values[1]) or Searchkey == self._key(self.values[2]):   #Als het gezochte item overeenkomt met 1 van de values uit self ==> Item is gevonden
            print("item found")
            return True
        else:                           #Als het item niet in self gevonden is.
            if self.isLeaf() == True:
                return False            #Self heeft geen kinderen ==> bijgevolg is het item niet gevonden
            elif self.values[0] != None and self.values[1] != None:     #Als self 2 data items bevat:
                if Searchkey < self._key(self.values[0]) and self.values[0] != None:   #Als het gezochte item kleiner is dan 1ste data item van self ==> zoek verder in linkerkind
                    if self.children[0] != None:
                        return self.children[0].retrieve(Searchkey)
                    else:
                        return False
                elif Searchkey < self._key(self.values[1]):                            #Als het gezochte item kleiner is dan het tweede data item van self ==> zoek in middenste kind
                    if self.children[1] != None:
                        return self.children[1].retrieve(Searchkey)
                    else:
                        return False
                else:                                                       #ALs het gezochte item groter is dan het tweede data item van self ==> zoek verder in rechterkind
                    if self.children[2] != None:
                        return self.children[2].retrieve(Searchkey)
                    else:
                        return False
            elif self.values[0] != None:                                #Als self 1 data item bevat:
                if Searchkey < self._key(self.values[0]):                              #Als het gezochte item kleiner is dan het data item van self ==> zoek verder in linkerkind
                    if self.children[0] != None:
                        return self.children[0].retrieve(Searchkey)
                    else:
                        return False
                else:
                    if self.children[2] != None:                            #Als het gezochte item groter is dan het data item van self ==> zoek verder in rechterkind
                        return self.children[2].retrieve(Searchkey)
                    else:
                        return False
            return False

    def inorderTraversal(self):
        '''Returns the tree in inorderTraversal way'''
        if self.children[0] == None and self.children[1] == None and self.children[2] == None and self.children[3] == None: #Als self een blad is ==> bezoek de items in het blad
            yield self.values[0]
            yield self.values[1]
            yield self.values[2]
        elif self.values[0] != None and self.values[1] != None:     #Als self 2 data items bevat ==> bezoek eerst het linkerkind dan het middenste kind en tenslotte het rechterkind
            if self.children[0] != None:
                yield from self.children[0].inorderTraversal()
            yield self.values[0]
            if self.children[1] != None:
                yield from self.children[1].inorderTraversal()
            yield self.values[1]
            if self.children[2] != None:
                yield from self.children[2].inorderTraversal()
        elif self.values[0] != None or self.values[1] != None:      #Als self 1 data item bevat ==> bezoek eerst het linkerkind en dan het rechterkind
            if self.children[0] != None:
                yield from self.children[0].inorderTraversal()
            yield self.values[0]
            if self.children[2] != None:
                yield from self.children[2].inorderTraversal()

class TwoThreeTree():
    def __init__(self, attribute):
        '''Makes an object of the class TwoThreeTree based on the TwoThreeTreeNode (see up)'''
        self._attribute = attribute
        self.root = Node(attribute)

    def attribute(self):
        '''Returns the attribute of the TwoThreeTree'''
        return self._attribute

    def isEmpty(self):
        '''Method to check if the tree is empty or not.'''
        if self.root.values[0] == None:
            return True
        else:
            return False

    def insert(self, NewItem):
        '''Inserts a new item in the TwoThreeTree, this operation is implemented in the TwoThreeTreeNode and returns this value'''
        return self.root.insert(NewItem)

    def inorder(self, visit = None):
        '''This operation is also implemented in the TwoThreeTreeNode and returns the value of this method'''
        yield from self.root.inorderTraversal()

    def sort(self, attr, sortFunc = sortingbubblesort):
        '''Returns a sorted list of the tree. This is done by generators and an inorderTraversal'''

        # TODO if attr == self._attribute you can yield from self.inorder()

        treeArray = list(self.inorder())
        treeArray = sortFunc(treeArray, attribute)
        for i in treeArray:
            yield i

    def retrieve(self, searchKey):
        '''Returns the value from the retrieve method of the TwoThreeTree if it is found and doesn't change the tree'''
        (succes, value) = self.root.retrieve(searchKey)
        return value

    def delete(self, searchKey):
        '''This operation is also implemented in the TwoThreeTreeNode and returns the value of this method'''
        if self.root.searchkey() == None:
            return False
        else:
            return self.root.delete(searchkey)

"""
A = Node(1)
A.insert(5)

#A.retrieve(1,1)
#print("inorder successor")
#A.delete(1,7)
#print(A.children[0].inorderSuccessor(1))
print(A)
"""
