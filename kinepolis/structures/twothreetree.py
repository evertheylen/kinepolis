#Auteur: Anthony Hermans
#Testen: Evert Heylen
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
        if len(self.children) > 3 and self.children[3] != None:
            output.append("other child:")
            output.append(self.children[3])
        return str(output)


    def searchkey(self):
        '''Return the searchkey of an item. This is the attribute of the item that is defined as the searchkey'''
        if self.values[0] == None and self.values[1] == None and self.values[2] == None:
            return None
        else:
            return self.values.__dict__[self.attribute]

    def isLeaf(self):
        if self.children[0] == None and self.children[1] == None and self.children[2] == None and self.children[3] == None:
            return True
        else:
            return False

    def split(self, attribute):
        '''Splits the node if necessary'''
        if self.parent == None:         #self is root
            print("swekker")
            self.children[0] = Node(attribute, [self.values[0],None,None], self, [self.children[0], None, self.children[1], None])
            self.children[1] = Node(attribute, [None,None,None], self, [None,None, None, None])
            self.children[2] = Node(attribute, [self.values[2],None,None], self, [self.children[2], None, self.children[3], None])
            self.children[3] = Node(attribute, [None,None,None], self, [None,None, None, None])
            self.values[0] = None
            self.values[2] = None
            return
        else:
            print("test")
            if self.parent.values[0] == None or self.parent.values[1] == None:
                print("ja")
                if self.values[0] != None and self.values[1] != None and self.values[2] != None:
                    print("double")
                    print(self.parent.values[1], self.values[1])
                    if self.values[1] <= self.parent.values[1]:
                        print("mcswek")
                        self.parent.values[0] = self.values[1]
                        self.parent.children[1].insert(attribute, self.values[2])
                        self.values[2] = None
                        self.values[1] = None
                        return
                    if self.values[1] > self.parent.values[1]:
                        print("three")
                        self.parent.values[0] = self.parent.values[1]
                        self.parent.values[1] = self.values[1]
                        self.parent.children[1].insert(attribute, self.values[0])
                        self.values[0] = None
                        self.values[1] = None
                        return
            else:
                print("3 in parent")
                if self.parent.values[0] == None or self.parent.values[1] == None:
                    if self.values[1] <= self.parent.values[0]:
                        temp = self.parent.values[0]
                        self.parent.values[2] = self.parent.values[1]
                        self.parent.values[1] = temp
                        self.parent.values[0] = self.values[1]
                        self.values[1] = None
                        return
                    elif self.values[1] > self.parent.values[0] and self.values[1] <= self.parent.values[1]:
                        self.parent.values[2] = self.parent.values[1]
                        self.parent.values[1] = self.values[1]
                        self.values[1] = None
                        return
                    elif self.values[1] > self.parent.values[1]:
                        self.parent.values[2] = self.values[1]
                        self.values[1] = None
                        return
                if self.parent.values[2] == None and self.parent.values[0] != None and self.parent.values[1] != None:
                    if self.values[1] < self.parent.values[0]:
                        self.parent.values[2] = self.parent.values[1]
                        self.parent.values[1] = self.parent.values[0]
                        self.parent.values[0] = self.values[1]
                        self.values[1] = None
                        self.parent.children[3] = self.parent.children[2]
                        self.parent.children[2] = self.parent.children[1]
                        self.parent.children[0] = Node(attribute, [self.values[0],None,None], self.parent, [self.children[0], None, self.children[1], None])
                        self.parent.children[1] = Node(attribute, [self.values[2],None,None], self.parent, [self.children[2], None, self.children[3], None])
                        self.parent.split(attribute)
                        return
                    if self.values[1] > self.parent.values[0] and self.values[1]<= self.parent.values[1]:
                        self.parent.values[2] = self.parent.values[1]
                        self.parent.values[1] = self.values[1]
                        self.values[1] = None
                        self.parent.children[3] = self.parent.children[2]
                        self.parent.children[2] = Node(attribute, [self.values[2],None,None], self.parent, [self.children[2], None, self.children[3], None])
                        self.parent.children[1] = Node(attribute, [self.values[0],None,None], self.parent, [self.children[0], None, self.children[1], None])
                        self.parent.children[0] = self.parent.children[0]
                        self.parent.split(attribute)
                        return
                    if self.values[1] > self.parent.values[1]:
                        self.parent.values[2] = self.values[1]
                        self.values[1] = None
                        self.parent.children[3] = Node(attribute, [self.values[2],None,None], self.parent, [self.children[2], None, self.children[3], None])
                        self.parent.children[2] = Node(attribute, [self.values[0],None,None], self.parent, [self.children[0], None, self.children[1], None])
                        self.parent.children[1] = self.parent.children[1]
                        self.parent.children[0] = self.parent.children[0]
                        self.parent.split(attribute)
                        return



    def insert(self, attribute, NewItem):
        '''Inserts a value in the TwoThreeTreeNode'''
        if self.children[0] == None and self.children[1] == None and self.children[2] == None and self.children[3] == None:     #isLeaf methode uit cursus
            if self.values[0] == None or self.values[1] == None or self.values[2] == None:
                if self.values[0] == None:
                    if self.values[2] == None:
                        self.values[0] = NewItem
                        return
                    else:
                        if self.values[2] <= NewItem:
                            temp = self.values[2]
                            self.values[2] = NewItem
                            self.values[0] = temp
                            return
                        else:
                            self.values[0] = NewItem
                            return
                if self.values[1] == None:
                    if self.values[2] == None:
                        if self.values[0] <= NewItem:
                            self.values[1] = NewItem
                            return
                        else:
                            temp = self.values[0]
                            self.values[0] = NewItem
                            self.values[1] = temp
                            return
                    else:
                        if NewItem >= self.values[0]:
                            if self.values[2] <= NewItem:
                                temp = self.values[2]
                                self.values[2] = NewItem
                                self.values[1] = temp
                                if self.values[0] != None and self.values[1] != None and self.values[2] != None:
                                    self.split(attribute)
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
                    if self.values[1] <= NewItem:
                        self.values[2] = NewItem
                        self.split(attribute)
                        return
                    else:
                        if self.values[1] >= NewItem:
                            temp = self.values[1]
                            self.values[1] = NewItem
                            self.values[2] = temp

                            if self.values[0] >= self.values[1]:
                                temp = self.values[0]
                                self.values[0] = self.values[1]
                                self.values[1] = temp
                        self.split(attribute)
                        return
        else:           #Het bevat kinderen
            if self.values[0] == None:
                if NewItem <= self.values[1]:
                    self.children[0].insert(attribute, NewItem)
                if NewItem > self.values[1]:
                    self.children[2].insert(attribute, NewItem)
            else:
                if NewItem < self.values[0]:
                    self.children[0].insert(attribute, NewItem)
                    return
                if NewItem <= self.values[1] and NewItem >= self.values[0]:
                    self.children[1].insert(attribute, NewItem)
                    return
                if NewItem > self.values[1]:
                    self.children[2].insert(attribute, NewItem)
                    return

    def fix(self, attribute):
        '''Fixes the node if necessary'''
        print("fixing the node")
        if self.parent == None:
            del self
        else:
            if self == self.parent.children[0]: #Herverdeling linkerkind
                if parent.children[1] != None and self.parent.children[1].values[0] != None and self.parent.children[1].values[1] != None:
                    temp = self.parent.values[0]
                    self.parent.values[0] = self.parent.children[1].values[0]
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
                    temp = self.parent.values[1]
                    self.parent.values[1] = self.parent.children[1].values[1]
                    self.parent.children[1].values[1] = None
                    self.values[1] = temp

    def delete(self, attribute, DeleteItem):
        '''Delete a the specific DeleteItem from the tree'''
        if DeleteItem == self.values[0] or DeleteItem == self.values[1]:
            print("Node is gevonden")
            if self.children[0] != None and self.children[1] != None and self.children[2] != None and self.children[3] != None: #Node is geen blad
                print("Node is geen blad")
                inorderSuccessor = self.inorderSuccessor(attribute, DeleteItem)
                if self.values[0] == DeleteItem:
                    delete = self.values[0]
                    self.values[0]  = inorderSuccessor
                    print(inorderSuccessor)
            if self.values[0] == None and self.values[1] == None:
                self.fix(attribute)
                success = True
                return success
        elif DeleteItem <= self.values[0] and self.children[0] != None:
            self.children[0].delete(attribute, DeleteItem)
            return
        if self.values[1] != None:
            if DeleteItem > self.values[0] and DeleteItem < self.values[1] and self.children[1] != None:
                self.children[1].delete(attribute, DeleteItem)
                return
            if DeleteItem > self.values[1] and self.children[2] != None:
                self.children[2].delete(attribute, DeleteItem)
                return
        else:
            success = False
            return success
    def inorderSuccessor(self, attribute, current):
        if self.children[0] == None and self.children[1] == None and self.children[2] == None and self.children[3] == None: #Node is een blad
            if self.values[1] != None:
                Successor = self.values[1]
                return Successor
            elif self.parent != None:
                self.parent.inorderSuccessor(attribute, current)
        if self.values[1] == None:
            if current < self.values[0] and self.children[0] != None:
                inorderSuccessor.children[0](attribute, current)
            if current > self.values[0] and self.children[2] != None:
                inorderSuccessor.children[2](attribute, current)
        if self.values[1] != None:
            if current < self.values[0] and self.children[0] != None:
                inorderSuccessor.children[0](attribute, current)
            if current < self.values[1] and self.children[1] != None:
                inorderSuccessor.children[1](attribute, current)
            if current > self.values[1] and self.children[2] != None:
                inorderSuccessor.children[2](attribute, current)

    def retrieve(self, attribute, Searchkey):
        '''Search the specific Searchkey in the tree, return True if Searchkey is found, otherwise return False'''
        if Searchkey == self.values[0] or Searchkey == self.values[1] or Searchkey == self.values[2]:   #Als het gezochte item overeenkomt met 1 van de values uit self ==> Item is gevonden
            print("item found")
            return True
        else:                           #Als het item niet in self gevonden is.
            if self.isLeaf == True:
                return False            #Self heeft geen kinderen ==> bijgevolg is het item niet gevonden
            elif self.values[0] != None and self.values[1] != None:     #Als self 2 data items bevat:
                if Searchkey < self.values[0] and self.values[0] != None:   #Als het gezochte item kleiner is dan 1ste data item van self ==> zoek verder in linkerkind
                    if self.children[0] != None:
                        return self.children[0].retrieve(attribute, Searchkey)
                    else:
                        return False
                elif Searchkey < self.values[1]:                            #Als het gezochte item kleiner is dan het tweede data item van self ==> zoek in middenste kind
                    if self.children[1] != None:
                        return self.children[1].retrieve(attribute, Searchkey)
                    else:
                        return False
                else:                                                       #ALs het gezochte item groter is dan het tweede data item van self ==> zoek verder in rechterkind
                    if self.children[2] != None:
                        return self.children[2].retrieve(attribute, Searchkey)
                    else:
                        return False
            elif self.values[0] != None:                                #Als self 1 data item bevat:
                if Searchkey < self.values[0]:                              #Als het gezochte item kleiner is dan het data item van self ==> zoek verder in linkerkind
                    if self.children[0] != None:
                        return self.children[0].retrieve(attribute, Searchkey)
                    else:
                        return False
                else:
                    if self.children[2] != None:                            #Als het gezochte item groter is dan het data item van self ==> zoek verder in rechterkind
                        return self.children[2].retrieve(attribute, Searchkey)
                    else:
                        return False
            return False

    def inorderTraversal(self, attribute):
        '''Returns the tree in inorderTraversal way'''
        if self.children[0] == None and self.children[1] == None and self.children[2] == None and self.children[3] == None: #Als self een blad is ==> bezoek de items in het blad
            yield (self.values[0],self.values[1],self.values[2])
        elif self.values[0] != None and self.values[1] != None:     #Als self 2 data items bevat ==> bezoek eerst het linkerkind dan het middenste kind en tenslotte het rechterkind
            if self.children[0] != None:
                yield from self.children[0].inorderTraversal(attribute)
            yield self.values[0]
            if self.children[1] != None:
                yield from self.children[1].inorderTraversal(attribute)
            yield self.values[1]
            if self.children[2] != None:
                yield from self.children[2].inorderTraversal(attribute)
        elif self.values[0] != None or self.values[1] != None:      #Als self 1 data item bevat ==> bezoek eerst het linkerkind en dan het rechterkind
            if self.children[0] != None:
                self.children[0].inorderTraversal(attribute)
            yield self.values[0]
            if self.children[2] != None:
                self.children[2].inorderTraversal(attribute)

class TwoThreeTree():
    def __init__(self, attribute, root=None):
        '''Makes an object of the class TwoThreeTree based on the TwoThreeTreeNode (see up)'''
        self._attribute = attribute
        self.root = Node(attribute, root)

    def attribute(self):
        '''Returns the attribute of the TwoThreeTree'''
        return self._attribute

    def isEmpty(self):
        '''Method to check if the tree is empty or not.'''
        if self.root.searchkey() == None:
            return True
        else:
            return False

    def insert(self, NewItem):
        '''Inserts a new item in the TwoThreeTree, this operation is implemented in the TwoThreeTreeNode and returns this value'''
        return self.rootItem.insert(self._attribute, NewItem)

    def inorder(self, visit = None):
        '''This operation is also implemented in the TwoThreeTreeNode and returns the value of this method'''
        yield from self.root.inorderTraversal(visit)

    def sort(self, attr, sortFunc = sortingbubblesort):
        '''Returns a sorted list of the tree. This is done by generators and an inorderTraversal'''
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
            return self.root.delete(searchkey, self)

A = Node(1)
#for i in range(8,1,-1):
    #print("inserting",i)
    #A.insert(1,i)
A.insert(1,89)
A.insert(1,90)
print(A)
A.delete(1,89)
A.inorderTraversal(1)
