
# wordt niet gebruikt, omdat het niet (volledig) werkt...

class Node:
    def __init__(self, info1 = None, info2 = None, info3 = None, child1 = None, child2 = None, child3 = None, child4 = None, parent = None):
        self.info1 = info1
        self.info2 = info2
        self.info3 = info3
        self.child1 = child1
        self.child2 = child2
        self.child3 = child3
        self.child4 = child4
        self.parent = parent

    def __repr__(self):
        return str(self.info1) + ", " + str(self.info2) + ", " + str(self.info3)

    def not__repr__(self):  #printmyself(self):
        print("My parent is: ", self.parent,".")
        print("My children are: [", self.child1,"], [",self.child2,"], [",self.child3,"], [",self.child4,"].")
        print("And my info is: ", self.info1,", ",self.info2,", ",self.info3)
        return

    def drawNode(self):
        print("\t\t\t\t[", self.parent,"]")
        print("\t\t\t[ ", self.info1,", ",self.info2,", ",self.info3,"]")
        print("\t[", self.child1,"]\t[",self.child2,"]\t[",self.child3,"]\t[",self.child4,"]\n")
        return

    def getLength(self):
        if self.info3 == None:
            if self.info2 == None:
                if self.info1 == None:
                    return 0
                else:
                    return 1
            else:
                return 2
        else:
            return 3

    def isLeaf(self):
        if self.child1 == None and self.child2 == None and self.child3 == None and self.child4 == None:
            return True
        return False

    def hasParent(self):
        if self.parent == None:
            return False
        else:
            return True

    def splitNode(self):
        # split the node:
        # the middle value goes up and gets the left and right value as it's children(second and third kids)
        # the left value gets child 1 and child 2
        # the right value gets child 3 and child 4
        if self.hasParent() == False:
            if self.isLeaf() == True:
                # make new children
                self.child1 = Node()
                self.child2 = Node()
                # put the correct values in the correct place
                self.child1.info1 = self.info1
                self.child2.info1 = self.info3
                # clear self
                self.info1 = self.info2
                self.info2 = None
                self.info3 = None
                # adjust the parent pointers
                self.child1.parent = self
                self.child2.parent = self
                return
                
            else:   # if self doesn't have a parent but has children
                # A = self.child1
                # B = self.child2
                # A.parent = Node()
                # A.parent.info1 = self.info1
                # B.parent = A.parent
                self.child1.parent = Node()             # give new parent, currently empty
                self.child1.parent.info1 = self.info1   # give the new node the left info of the 4-node
                self.child2.parent = self.child1.parent # the new parent is also the parent of child2
                self.child1.parent.child1 = self.child1 # child1 of the new node is now the original child1
                self.child1.parent.child2 = self.child2 # child2 of the new node is now the original child2

                self.child3.parent = Node()             # give new parent, currently empty
                self.child3.parent.info1 = self.info3   # give the new node the right info of the 4-node
                self.child4.parent = self.child3.parent # the new parent is also the parent of child4
                self.child3.parent.child1 = self.child3 # child1 of the new node is now the original child3
                self.child3.parent.child2 = self.child4 # child2 of the new node is now the original child4
                # assign self's new children 
                self.child1 = self.child1.parent
                self.child2 = self.child3.parent
                self.child3 = None
                self.child4 = None
                # the new parent is self
                self.child1.parent = self
                self.child2.parent = self
                # clear self
                self.info1 = self.info2
                self.info2 = None
                self.info3 = None
                return
                
        else: # if self has a parent
            if self.isLeaf() == True:
                if self.parent.getLength() == 1:    # if the parent is a 2-node
                    if self.parent.child2 == self:
                        self.parent.child3 = Node()
                        self.parent.child3.info1 = self.info3   # put the old, right info into the new child
                        self.parent.info2 = self.info2
                        self.parent.child3.parent = self.parent
                        self.info2 = None
                        self.info3 = None
                        return
                        
                    if self.parent.child1 == self:
                        # make child2 the child3
                        self.parent.child3 = self.parent.child2
                        self.parent.child3.parent = self.parent
                        self.parent.child2 = Node()
                        self.parent.child2.info1 = self.info3
                        self.parent.child2.parent = self.parent
                        self.parent.info2 = self.parent.info1
                        self.parent.info1 = self.info2
                        self.info2 = None
                        self.info3 = None
                        return

                if self.parent.getLength() == 2:
                    if self.parent.child1 == self:
                        # move children
                        self.parent.child4 = self.parent.child3
                        self.parent.child4.parent = self.parent
                        self.parent.child3 = self.parent.child2
                        self.parent.child4.parent = self.parent
                        # make new node = child2
                        self.parent.child2 = Node()
                        self.parent.child2.parent = self.parent
                        # put info into the new node
                        self.parent.child2.info1 = self.info3
                        # put info into the parent
                        self.parent.info3 = self.parent.info2
                        self.parent.info2 = self.info2
                        self.info2 = None
                        self.info3 = None
                        return
                    if self.parent.child2 == self:
                        self.parent.child4 = self.parent.child3
                        self.parent.child4.parent = self.parent
                        self.parent.child3 = Node()
                        self.parent.child3.parent = self.parent
                        self.parent.child3.info1 = self.info3
                        self.parent.info3 = self.parent.info2
                        self.parent.info2 = self.info2
                        self.info2 = None
                        self.info3 = None
                        return
                    if self.parent.child3 == self:
                        self.parent.child4 = Node()
                        self.parent.child4.parent = self.parent
                        self.parent.child4.info1 = self.info3
                        self.parent.info3 = self.info2
                        self.info2 = None
                        self.info3 = None
                        return

            else:   # if self is not a leaf and has a parent
                if self.parent.getLength() == 1:
                    self.child1.parent = Node()
                    self.child1.parent.parent = self.parent
                    self.child2.parent = self.child1.parent
                    self.child1.parent.child1 = self.child1
                    self.child1.parent.child2 = self.child2

                    if self.parent.child1 == self:
                        self.parent.child1 = self.child1.parent
                        self.parent.child3 = self.parent.child2
                        self.parent.child2 = self
                        self.child1.parent.info1 = self.info1
                        self.parent.info2 = self.info2
                        self.info1 = info3

                    if self.parent.child2 == self:
                        self.parent.child2 = self.child1.parent
                        self.parent.child3 = self
                        self.child1.parent.info1 = self.info1
                        self.parent.info2 = self.info2
                        self.info1 = self.info3

                    self.child1 = self.child3
                    self.child2 = self.child4
                    self.child3 = None
                    self.child4 = None
                    self.info2 = None
                    self.info3 = None
                    return
                        
                elif self.parent.getLength() == 2:
                    self.child1.parent = Node()
                    self.child1.parent.parent = self.parent
                    self.child2.parent = self.child1.parent
                    self.child1.parent.child1 = self.child1
                    self.child1.parent.child2 = self.child2

                    if self.parent.child1 == self:
                        self.parent.child1 = self.child1.parent
                        self.parent.child4 = self.parent.child3
                        self.parent.child3 = self.parent.child2
                        self.parent.child2 = self
                        self.child1.parent.info1 = self.info1
                        self.parent.info3 = self.parent.info2
                        self.parent.info2 = self.info2
                        self.info1 = self.info3

                    if self.parent.child2 == self:
                        self.parent.child2 = self.child1.parent
                        self.parent.child4 = self.parent.child3
                        self.parent.child3 = self
                        self.child1.parent.info1 = self.info1
                        self.parent.info3 = self.parent.info2
                        self.parent.info2 = self.info2
                        self.info1 = self.info3

                    if self.parent.child3 == self:
                        self.parent.child3 = self.child1.parent
                        self.parent.child4 = self
                        self.child1.parent.info1 = self.info1
                        self.parent.info3 = self.info2
                        self.info1 = self.info3

                    self.child1 = self.child3
                    self.child2 = self.child4
                    self.child3 = None
                    self.child4 = None
                    self.info2 = None
                    self.info3 = None

                    return

    def insert(self,newInfo):
        if newInfo in [self.info1,self.info2,self.info3]:
            return False

        if self.getLength() == 0:
            self.info1 = newInfo
            return True

        elif self.getLength() == 1:
            if self.isLeaf() == True:
                self.info2 = newInfo
                return True
            else:
                if newInfo < self.info1:
                    return self.child1.insert(newInfo)
                else:
                    
                    return self.child2.insert(newInfo)

        elif self.getLength() == 2:
            if self.isLeaf() == True:
                self.info3 = newInfo
                return True
            else:
                if newInfo < self.info1:
                    return self.child1.insert(newInfo)
                else:
                    if newInfo < self.info2:
                        return self.child2.insert(newInfo)
                    else:
                        return self.child3.insert(newInfo)

        elif self.getLength() == 3:
            self.splitNode()
            if self.hasParent() == True:
                if self.parent.getLength() == 3:
                    if newInfo < self.parent.info1:
                        self.parent.child1.insert(newInfo)
                    if newInfo < self.parent.info2:
                        self.parent.child2.insert(newInfo)
                    if newInfo < self.parent.info3:
                        self.parent.child3.insert(newInfo)
                    else:
                        self.parent.child4.insert(newInfo)
            else:
                self.insert(newInfo)
            return True

    def inorderTraversal(self):
        if self.isLeaf():
                for i in [self.info1, self.info2, self.info3]:
                    if i!=None:
                        yield i
        else:
            if self.getLength() == 1:
                yield from self.child1.inorderTraversal()
                yield self.info1
                yield from self.child2.inorderTraversal()
            elif self.getLength() == 2:
                yield from self.child1.inorderTraversal()
                yield self.info1
                yield from self.child2.inorderTraversal()
                yield self.info2
                yield from self.child3.inorderTraversal()
            elif self.getLength() == 3:
                yield from self.child1.inorderTraversal()
                yield self.info1
                yield from self.child2.inorderTraversal()
                yield self.info2
                yield from self.child3.inorderTraversal()
                yield self.info3
                yield from self.child4.inorderTraversal()

    def retrieve(self,data):
        children = [self.child1,self.child2,self.child3,self.child4]
        infolst = [self.info1,self.info2,self.info3]
        if data in infolst:
            return data
        elif self.isLeaf() == True:
            return None
        elif self.getLength() == 3:
            if data < self.info1:
                return self.child1.retrieve(data)
            elif data < self.info2:
                return self.child2.retrieve(data)
            elif data < self.info3:
                return self.child3.retrieve(data)
            else:
                return self.child4.retrieve(data)
        elif self.getLength() == 2:
            if data < self.info1:
                return self.child1.retrieve(data)
            elif data < self.info2:
                return self.child2.retrieve(data)
            else:
                return self.child3.retrieve(data)
        elif self.getLength() == 1:
            if data < self.info1:
                return self.child1.retrieve(data)
            else:
                return self.child2.retrieve(data)

    def findNode(self,data):
        infolst = [self.info1,self.info2,self.info3]
        if data in infolst:
            return self

        if self.getLength() == 1:   # self is 2-node
            if self.isLeaf() == True:
                return False
            else:
                if data < self.info1:
                    return self.child1.findNode(data)
                else:
                    return self.child2.findNode(data)

        if self.getLength() == 2:   # self is 3-node
            if self.isLeaf() == True:
                return False
            else:
                if data < self.info1:
                    return self.child1.findNode(data)
                elif data < self.info2:
                    return self.child2.findNode(data)
                else:
                    return self.child3.findNode(data)

        if self.getLength() == 3:   # self is 4-node
            if self.isLeaf() == True:
                return False
            else:
                if data < self.info1:
                    return self.child1.findNode(data)
                elif data < self.info2:
                    return self.child2.findNode(data)
                elif data < self.info3:
                    return self.child3.findNode(data)
                else:
                    return self.child4.findNode(data)

    def removeLeafData(self,data):
        if self.info1 == data:
            self.info1 = self.info2
            self.info2 = self.info3
            self.info3 = None
        elif self.info2 == data:
            self.info2 = self.info3
            self.info3 = None
        elif self.info3 == data:
            self.info3 = None

    def checkRotate(self):
        if self.parent.child1 == self:
            if self.parent.child2.getLength() > 1:
                return True
        elif self.parent.child2 == self:
            if self.parent.child1.getLength() > 1:
                return True
            if self.parent.child3 != None:
                if self.parent.child3.getLength() > 1:
                    return True
        elif self.parent.child3 == self:
            if self.parent.child2.getLength() > 1:
                return True
            if self.parent.child4 != None:
                if self.parent.child4.getLength() > 1:
                    return True
        elif self.parent.child4 == self:
            if self.parent.child3.getLength() > 1:
                return True

        return False
                    
    def delete(self, data):
        # if the root has 2 children that are also 2-nodes, make a 4-node
        if self.hasParent() == False:   # if self is the root
            if self.getLength() == 1:   # if the root is a 2-node
                if self.child1 != None: # if the root has children
                    if self.child1.getLength() == 1:
                        if self.child2.getLength() == 1:
                            # if the root is a 2-node and it's children are too, then you merge them together!
                            self.info2 = self.info1         # merge info's together
                            self.info1 = self.child1.info1
                            self.info3 = self.child2.info1
                            self.child1 = self.child1.child1    # the child of self's previous child is now self's child
                            self.child2 = self.child1.child2
                            self.child3 = self.child2.child1
                            self.child4 = self.child2.child2
                            self.child1.parent = self       #adjust parent pointers
                            self.child2.parent = self
                            self.child3.parent = self
                            self.child4.parent = self
                            # merge complete
                            self.delete(data)


        if self.hasParent() == True:    
            if self.getLength() == 1: # if you encounter a 2-node: check for the adjacent siblings...
                                      # if one of the siblings has a node on overshot, make it the parent and get the parents info
                if self.parent.child1 == self:
                    if self.parent.child2.getLength() > 1:# take from child2
                        self.info2 = self.parent.info1
                        self.parent.info1 = self.parent.child2.info1
                        self.parent.child2.info1 = self.parent.child2.info2
                        self.parent.child2.info2 = self.parent.child2.info3
                        self.parent.child2.info3 = None
                        self.delete(data)
                        
                if self.parent.child2 == self:
                    if self.parent.child1.getLength() > 1:# take from child1
                        self.info2 = self.parent.info1
                        if self.parent.child1.info3 != None:
                            self.parent.info1 = self.parent.child1.info3
                            self.parent.child1.info3 = None
                        elif self.parent.child1.info2 != None:
                            self.parent.info1 = self.parent.child1.info2
                            self.parent.child1.info2 = None
                        self.delete(data)
                        
                    elif self.parent.child3 != None:# take from child3
                        if self.parent.child3.getLength() > 1:
                            self.info2 = self.parent.info2
                            self.parent.info2 = self.parent.child3.info1
                            self.parent.child3.info1 = self.parent.child3.info2
                            self.parent.child3.info2 = self.parent.child3.info3
                            self.parent.child3.info3 = None
                        self.delete(data)

                if self.parent.child3 == self:
                    if self.parent.child2.getLength() > 1:#take from child2
                        self.info2 = self.info1
                        self.info1 = self.parent.info2
                        if self.parent.child2.info3 != None:
                            self.parent.info2 = self.parent.child2.info3
                            self.parent.child2.info3 = None
                        elif self.parent.child2.info2 != None:
                            self.parent.info2 = self.parent.child2.info2
                            self.parent.child2.info2 = None
                        self.delete(data)

                    elif self.parent.child4 != None:
                        if self.parent.child4.getLength() > 1:
                            self.info2 = self.parent.info2
                            self.parent.info2 = self.parent.child4.info1
                            self.parent.child4.info1 = self.parent.child4.info2
                            self.parent.child4.info2 = self.parent.child4.info3
                            self.parent.child4.info3 = None
                            self.delete(data)
                            # take from child4: get the first info from child4 and shift its info's to the left by 1
                if self.parent.child4 == self:#take from child4
                    if self.parent.child3.getLength() > 1:
                        self.info2 = self.info1
                        self.info1 = self.parent.info3
                        if self.parent.child3.info3 != None:
                            self.parent.info3 = self.parent.child3.info3
                            self.parent.child3.info3 = None
                        elif self.parent.child3.info2 != None:
                            self.parent.info3 = self.parent.child3.info2
                            self.parent.child3.info2 = None
                        self.delete(data)
                
                else:   # no adjacent sibling can miss an info, take info from the parent and adjust the children
                    if self.parent.getLength() == 2:
                        if (self.parent.child1 == self) or (self.parent.child2 == self):
                            self.info2 = self.parent.info1
                            self.parent.info1 = self.parent.info2
                            self.parent.info2 = None
                        else:
                            self.info2 = self.parent.info2
                            self.parent.info2 = None
                        self.delete(data)
                    elif self.parent.getLength() == 3:
                        if self.parent.child1 == self:
                            self.info2 = self.parent.info1
                            self.parent.info1 = self.parent.info2
                            self.parent.info2 = self.parent.info3
                            self.parent.info3 = None

                            self.child3 = self.parent.child2
                            self.child3.parent = self
                            self.parent.child2 = self.parent.child3
                            self.parent.child3 = self.parent.child4
                            self.parent.child4 = None
                            self.delete(data)

                        elif self.parent.child2 == self:
                            self.info2 = self.parent.info2
                            self.parent.info2 = self.parent.info3
                            self.parent.info3 = None

                            self.child3 = self.parent.child3
                            self.child3.parent = self
                            self.parent.child3 = self.parent.child4
                            self.parent.child4 = None
                            self.delete(data)

                        elif self.parent.child3 == self:
                            self.info2 = self.parent.info2
                            self.parent.info2 = self.parent.info3
                            self.parent.info3 = None


                            self.child2 = self.child1
                            self.child3 = self.child2
                            self.child1 = self.parent.child2
                            self.child3.parent = self
                            self.parent.child2 = self
                            self.parent.child3 = self.parent.child4
                            self.parent.child4 = None
                            self.delete(data)

                        elif self.parent.child4 == self:
                            self.info2 = self.parent.info3
                            self.parent.info3 = None

                            self.child2 = self.child1
                            self.child3 = self.child2
                            self.child1 = self.parent.child3
                            self.child1.parent = self
                            self.parent.child3 = self
                            self.parent.child4 = None
                            self.delete(data)

                        


class twoThreeFourTree:
    def __init__(self):
        self.root = Node()

    def __repr__(self):
        return str(list(self.inorder()))

    def insert(self,newInfo):
        return self.root.insert(newInfo)

    def inorder(self):
        yield from self.root.inorderTraversal()

    def delete(self,data):
        return self.root.delete(data)

    def isEmpty(self):
        if self.root.info1 == None and self.root.info2 == None and self.root.info3 == None:
            return True
        else:
            return False
       
    def retrieve(self, data):
        return self.root.retrieve(data)