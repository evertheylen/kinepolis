class Node:
    def __init__(self, attribute, item = None, next = None, leftpointer = None, rightpointer = None, leftchild = None, rightchild = None, parent = None):
        '''The standard python initializer. With all the aspects of a redblack node.'''
        self.item = item
        self.next = next
        self.leftpointer = leftpointer
        self.rightpointer = rightpointer
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.parent = parent
        self.attribute = attribute
    
    def searchkey(self):
        if self.item == None:
            return None
        return self.item.__dict__[self.attribute]
    
    def __le__(self, t2):
        '''Operator overloading for lesser then or equal.'''
        return self.searchkey() <= t2.searchkey()
        
    def __ge__(self, t2):
        '''Operator overloading for greater then or equal.'''
        return self.searchkey() >= t2.searchkey()
        
    def __lt__(self, t2):
        '''Operator overloading for lesser then.'''
        return self.searchkey() < t2.searchkey()
        
    def __gt__(self, t2):
        '''Operator overloading for greater then.'''
        return self.searchkey() > t2.searchkey()
                
    def __repr__(self):
        '''Operator overloading for the visual representation of a Node when it gets printed.'''
        if self.item != None:
            output = str(self.searchkey())
        else:
            return ('Empty node')
        if self.next != None:
            output += ', '+str(self.next)
        return output
        
    def insert(self, attribute, newItem, tree):
        '''Insert method for one Node. Tree is an argument for the use of fix_rotation later in this method.'''
        tempNode = Node(attribute, newItem)
        if self.fix_rotation(tree) == 1:
            # If this equals 1 than the order of the tree is changed and the original position of self is now its parent.
            return self.parent.insert(attribute, newItem, tree)
        else:
            if newItem == self.item:
                self.treeItem = self.item
                print('Error: Er bevindt zich al een item met deze zoeksleutel in de boom!')
                return False
                
            if self.item == None:
                # If the tree is empty then a new root is made.
                self.item = newItem
                return True
                
            elif self.leftchild == None and newItem.__dict__[self.attribute] < self.searchkey():
                # If the location were newitem should be placed is on the left of the current Item and that location is empty then newItem gets placed there.
                if self.fix_rotation(tree) == 1:
                    # If the order of the tree has changed then insert gets redone to see if this location is still free or not.
                    self.insert(attribute, newItem, tree)
                self.leftchild = tempNode
                self.leftpointer = 'red'
                tempNode.parent = self
                #Insert and reorder the tree afterwards.
                tree.rootItem.fix_rotation(tree)
                return True
                
            elif self.rightchild == None and newItem.__dict__[self.attribute] > self.searchkey():
                # Same as the left insert but on the right.
                if self.fix_rotation(tree) == 1:
                    self.insert(attribute, newItem, tree)        
                self.rightchild = tempNode
                self.rightpointer = 'red'
                tempNode.parent = self
                tree.rootItem.fix_rotation(tree)          
                return True  
                    
            else:
                # If we aren't in a leaf then we pick the correct side based on the searchalgorithm, we reorder the tree on that side and we run the insert algorithm for the next leaf.
                if newItem.__dict__[self.attribute] < self.searchkey():
                    if self.leftchild.fix_rotation(tree) == 1:
                        return self.leftchild.parent.insert(attribute, newItem, tree)
                    else:
                    
                        return self.leftchild.insert(attribute, newItem, tree)
                else:
                    if self.rightchild.fix_rotation(tree) == 1:

                        return self.rightchild.parent.insert(attribute, newItem, tree)
                    else:                        

                        return self.rightchild.insert(attribute, newItem, tree)
                                
        
    def inorderTraversal(self, visit):
        '''The inorderTraversal is just a recursive algorithm. It prints out the left most subtree of a tree, then the root and then the rightmost subtree. If we do that. The tree is printed out in order.'''
        if self.searchkey != None and self.leftchild == None and self.rightchild == None:
            if visit != None:
                visit()
            self.leftpointer = None                                         #Makes sure there are no pointers left over after some rotation.
            self.rightpointer = None
            yield self.item  
        else:
            if self.leftchild != None:
                for i in self.leftchild.inorderTraversal(visit):
                    yield i
            if visit != None:
                visit()
            yield self.item
            if self.rightchild != None:
                for i in self.rightchild.inorderTraversal(visit):                     # Then the rightsubtree.
                    yield i

    def retrieve(self, searchKey):
        '''The retrieve method looks for a searchKey and returns that searchkey if it is in the tree.If it isn't it returns False.'''
        treeItem = self.find_searchKey(searchKey)
        if treeItem != None:    
            return True, treeItem.item
        else:
            return False, treeItem
                
    def find_searchKey(self, searchKey):
        '''This function is used to find the location of an item in the tree. It returns the node with all its atributes.'''
        if searchKey == self.searchkey():                                          #The basecase of the recursive algorithm: if the current location has the correct searchKey then that is the item that we are looking for.
            itemLocation = self
            return itemLocation
        
        elif self.leftchild == None and searchKey < self.searchkey():              #Two only possible ways that the searchKey we are looking for is not in the tree.
            return None
            
        elif self.rightchild == None and searchKey > self.searchkey():
            return None   
        
        else:
            if searchKey < self.searchkey():                                       # Standard binary search algorith.
                return self.leftchild.find_searchKey(searchKey)
            else:
                return self.rightchild.find_searchKey(searchKey)
                    
    def find_successor(self, successorlist):   
        '''The method find_successor returns the inorder succesorlist of the item. Its a list of all the items in the tree. In the deletealgorithm this list gets sorted and the inorder successor can be determined. It traverses the tree using an inorderTraversal.'''
        if self.searchkey != None and self.leftchild == None and self.rightchild == None:
            successorlist.append(self)
        else:
            if self.leftchild != None:
                self.leftchild.find_successor(successorlist)
            successorlist.append(self)
            if self.rightchild != None:
                self.rightchild.find_successor(successorlist)        
    
    def fixdoubleblack(self, tree):
        '''Fix double black is a different way of looking at a delete. I have based myself on another way than in the course material but I found it easier to code. Basically it looks at the pointer of siblings and parents and it makes some of them a doubleblack pointer. This isn't allowed in the tree and this function gets rid of them by rotating and color changing.'''
        if self.parent.leftpointer == 'blackblack':                         #This is the part for a left doubleblack pointer, the part of the right one is exactly the same but mirrored. 
            if self.parent.leftchild.leftchild == None and self.parent.leftchild.rightchild == None:
                self.parent.leftchild = None
                self.parent.leftpointer = None
            else:
                self.parent.leftpointer = 'black'                
            if self.parent.rightpointer == 'red':                           # if the sibling is red, then rotate so that a black node becomes the new sibling, then treat it as a black-sibling case.
                self.parent.forcedrotateleft(tree)
            if self.parent.rightpointer == 'black':                         #If the sibling is black:
                if (self.parent.rightchild.leftpointer == 'black' or self.parent.rightchild.leftpointer == None) and (self.parent.rightchild.rightpointer == 'black' or self.parent.rightchild.rightpointer == None):                                                                   #If both its children are black (No children = black).
                    self.parent.rightpointer = 'red'                        #The sibling gets recolored.
                    #self.parent.leftpointer = None                          #The node that needs to be deleted gets erased.
                    #self.parent.leftchild = None
                    if self.parent.parent != None and self.parent.parent.leftchild == self.parent:  
                        if self.parent.parent.leftpointer == 'red':         # The parent gets recolored too.
                            self.parent.parent.leftpointer = 'black' 
                        else:
                            self.parent.parent.leftpointer = 'blackblack'   #If the parent was black, now he is doubleblack. So we call the fixdoubleblack on the parent.
                            self.parent.fixdoubleblack(tree)
                    elif self.parent.parent != None and self.parent.parent.rightchild == self.parent:                                                   #Same for a right parent.
                        if self.parent.parent.rightpointer == 'red':    
                            self.parent.parent.rightpointer = 'black'
                        else:
                            self.parent.parent.rightpointer = 'blackblack'
                            self.parent.fixdoubleblack(tree)
                elif self.parent.rightchild.rightpointer == 'red':          #If the sibling is black and its rightchild (its 'nephew') is red.
                    self.parent.forcedrotateleft(tree)                      #Rotate and recolor the red 'nephew' that is involved in the rotation.
                    #self.parent.leftpointer = None
                    #self.parent.leftchild = None
                    self.parent.parent.rightpointer = 'black'
                elif self.parent.rightchild.leftpointer == 'red':           #Same for a leftchild.
                    self.parent.forcedrotateright2(tree)
                    #self.parent.leftpointer = None
                    #self.parent.leftchild = None
                    self.parent.parent.rightpointer = 'black'
                    
        else:       #Right double black pointer.
            if self.parent.rightchild.leftchild == None and self.parent.rightchild.rightchild == None:
                self.parent.rightchild = None
                self.parent.rightpointer = None
            else:
                self.parent.rightpointer = 'black'
            if self.parent.leftpointer == 'red':
                self.parent.forcedrotateright(tree)
            if self.parent.leftpointer == 'black':
                if (self.parent.leftchild.rightpointer == 'black' or self.parent.leftchild.rightpointer == None) and (self.parent.leftchild.leftpointer == 'black' or self.parent.leftchild.leftpointer == None):
                    self.parent.leftpointer = 'red'
                    #self.parent.rightpointer = None
                    #self.parent.rightchild = None
                    if self.parent.parent != None and self.parent.parent.leftchild == self.parent:
                        if self.parent.parent.leftpointer == 'red':
                            self.parent.parent.leftpointer = 'black'
                        else:
                            self.parent.parent.leftpointer = 'blackblack'
                            self.parent.fixdoubleblack(tree)
                    elif self.parent.parent != None and self.parent.parent.rightchild == self.parent:
                        if self.parent.parent.rightpointer == 'red':
                            self.parent.parent.rightpointer = 'black'
                        else:
                            self.parent.parent.rightpointer = 'blackblack'
                            self.parent.fixdoubleblack(tree)
                elif self.parent.leftchild.leftpointer == 'red':
                    self.parent.forcedrotateright(tree)
                    #self.parent.rightpointer = None
                    #self.parent.rightchild = None
                    self.parent.parent.leftpointer = 'black'
                elif self.parent.leftchild.rightpointer == 'red':
                    self.parent.forcedrotateleft2(tree)
                    #self.parent.rightpointer = None
                    #self.parent.rightchild = None
                    self.parent.parent.leftpointer = 'black'
    def delete(self, searchKey, tree):
        '''The main delete function of the node. It finds the inorder successor and based on the location of the leaf that needs to be deleted it swaps it or not.'''
        itemLocation = self.find_searchKey(searchKey)                       #Find the node n that contains the value to be deleted.
        if itemLocation == None:
            print("Het item dat u wilt deleten bevindt zich niet in de boom.")
            return False
        successorlist = []
        self.find_successor(successorlist)                                  #The inorder successor is the item : self < inordersuccessor and self >= everything which is < inorder successor            
        successor = None
        for i in range(len(sorted(successorlist))-1):                       #find the inorder successor of the item.
            if sorted(successorlist)[i].searchkey() == searchKey:
                successor = sorted(successorlist)[i+1]
        if successor == None:
            successor = sorted(successorlist)[-1]
        successorLocation = self.find_searchKey(successor.searchkey())             #The succesor is found.
        if itemLocation.leftchild == None and itemLocation.rightchild == None:
            #If node to be deleted is a red leaf, remove leaf, done.
            if itemLocation.parent != None:
                if itemLocation < itemLocation.parent and itemLocation.parent.leftpointer == 'red':
                    itemLocation.parent.leftchild = None
                    itemLocation.parent.leftpointer = None
                elif itemLocation > itemLocation.parent and itemLocation.parent.rightpointer == 'red':
                    itemLocation.parent.rightchild = None
                    itemLocation.parent.rightchild = None
                elif itemLocation < itemLocation.parent and itemLocation.parent.leftpointer == 'black':
                #The node itself is a black leaf
                    itemLocation.searchkey() = None
                    itemLocation.parent.leftpointer = 'blackblack'  #Make the parent a doubleblack pointer and go to the fixdoubleblack algorithm.
                    itemLocation.fixdoubleblack(tree)
                elif itemLocation > itemLocation.parent and itemLocation.parent.rightpointer == 'black':
                    itemLocation.searchkey() = None
                    itemLocation.parent.rightpointer = 'blackblack'
                    itemLocation.fixdoubleblack(tree)
            else:
                tree.rootItem = None        #If it is the last item in the tree.
        elif itemLocation.leftchild == None or itemLocation.rightchild == None:
            #If it is a single-child parent, replace with its child.
            if itemLocation.rightchild == None:
                if itemLocation.parent == None:
                    tree.rootItem = itemLocation.leftchild
                    itemLocation.leftchild.parent = None
                else:
                    if itemLocation < itemLocation.parent:
                        itemLocation.parent.leftchild = itemLocation.leftchild
                        itemLocation.leftchild.parent = itemLocation.parent
                        itemLocation.parent.leftpointer = 'black'
                    else:
                        itemLocation.parent.rightchild = itemLocation.leftchild
                        itemLocation.leftchild.parent = itemLocation.parent
                        itemLocation.parent.rightpointer = 'black' 
            else:
                if itemLocation.parent == None:
                    tree.rootItem = itemLocation.rightchild
                    itemLocation.rightchild.parent = None
                else:
                    if itemLocation < itemLocation.parent:
                        itemLocation.parent.leftchild = itemLocation.rightchild
                        itemLocation.rightchild.parent = itemLocation.parent
                        itemLocation.parent.leftpointer = 'black'
                    else:
                        itemLocation.parent.rightchild = itemLocation.rightchild
                        itemLocation.rightchild.parent = itemLocation.parent
                        itemLocation.parent.rightpointer = 'black'
     
        else:     
            #If it has two internal nodes, swap with successor.
            successorLocation.originalparent = successor.parent.item                 
            tempItem = successor.item                           #Swap the item and its successor
            successorLocation.item = itemLocation.item
            itemLocation.item = tempItem
            if successorLocation.parent != None:
                if itemLocation.item < successorLocation.originalparent and successorLocation.parent.leftpointer == 'red':                  #If the inorder successor is red, it must be a leaf so we just remove the leaf.
                    successorLocation.parent.leftchild = None
                    successorLocation.parent.leftpointer = None
                elif itemLocation.item > successorLocation.originalparent and successorLocation.parent.rightpointer == 'red':  
                    successorLocation.parent.rightchild = None
                    successorLocation.parent.rightpointer = None
                    
                elif successorLocation.leftchild != None and successorLocation.rightchild == None:
                    # If the inorder successor is a single child parent we can do the same algorithm as if the searchKey was a single child parent.
                    if successorLocation.parent == None:
                        tree.rootItem = successorLocation.leftchild
                        successorLocation.leftchild.parent = None
                    else:
                        if itemLocation.item < successorLocation.originalparent:
                            successorLocation.parent.leftchild = successorLocation.leftchild
                            successorLocation.leftchild.parent = successorLocation.parent
                            successorLocation.parent.leftpointer = 'black'
                        else:
                            successorLocation.parent.rightchild = successorLocation.leftchild
                            successorLocation.leftchild.parent = successorLocation.parent
                            successorLocation.parent.rightpointer = 'black' 
                elif successorLocation.rightchild != None and successorLocation.rightchild == None:
                    if successorLocation.parent == None:
                        tree.rootItem = successorLocation.rightchild
                        successorLocation.rightchild.parent = None
                    else:
                        if itemLocation.item < successorLocation.originalparent:
                            successorLocation.parent.leftchild = successorLocation.rightchild
                            successorLocation.rightchild.parent = successorLocation.parent
                            successorLocation.parent.leftpointer = 'black'
                        else:
                            successorLocation.parent.rightchild = successorLocation.rightchild
                            successorLocation.rightchild.parent = successorLocation.parent
                            successorLocation.parent.rightpointer = 'black'
                      
                else:
                    #If the in-order successor is a black leaf. Then we make the successor a double black leaf and we do fixdoubleblack on it.
                    
                    if itemLocation.item < successorLocation.originalparent and successorLocation.parent.leftpointer == 'black':
                        successorLocation.item = None
                        successorLocation.parent.leftpointer = 'blackblack'
                        successorLocation.fixdoubleblack(tree)
                    elif itemLocation.item > successorLocation.originalparent and successorLocation.parent.rightpointer == 'black':
                        successorLocation.item = None
                        successorLocation.parent.rightpointer = 'blackblack'
                        successorLocation.fixdoubleblack(tree)             

    def forcedrotateleft(self, tree):
        '''The function forced rotate left is basically an inward rotation to the left but without the checks if it needs to be done or not, therefore it is forced. It is used in the fix_doubleblack function.'''
        originalself = self                                             #Sets all the original positions in a save spot. They can be used later in the algorithm without the fear of the value that may have been changed due to the rotation. It is easier to correctly change the order of the tree if I have these original variables. The same principle is also used in the rest of the rotations.
        originalselfright = self.rightchild
        originalselfleft = self.leftchild
        originalselflpoint = self.leftpointer
        originalselfrpoint = self.rightpointer
        originalselfrightright = self.rightchild.rightchild
        originalselfrightleft = self.rightchild.leftchild
        originalparent = self.parent

        self.rightchild = originalselfrightleft                         #Actual start of the rotation.                          
        if originalselfrightleft != None:
            originalselfrightleft.parent = self         
        self.rightpointer = originalselfright.leftpointer
        self.parent = originalselfright
        self.parent.leftpointer = originalselfrpoint            
        originalselfright.leftchild = self
        originalselfright.parent = originalparent  
        if originalparent != None and originalself > originalparent:
            originalparent.leftchild = originalselfright
        elif originalparent != None and originalself < originalparent:               
            originalparent.rightchild = originalselfright                
        if originalparent == None:                                      #If the original parent was None then it was the root of the tree that participated in this rotation and therefore we have a new root. To make this clear to the rest of the program I return a 1.
            tree.rootItem = self.parent
            return 1
    
    def forcedrotateright(self, tree):                
        '''Forced inward rotation to the right.'''
        originalself = self
        originalselfright = self.rightchild
        originalselfleft = self.leftchild
        originalselflpoint = self.leftpointer
        originalselfrpoint = self.rightpointer
        originalselfleftright = self.leftchild.rightchild
        originalselfleftleft = self.leftchild.leftchild
        originalparent = self.parent

        self.leftchild = originalselfleftright
        if originalselfleftright != None:
            originalselfleftright.parent = self 
        self.leftpointer = originalselfleft.rightpointer
        self.parent = originalselfleft
        self.parent.rightpointer = originalselflpoint
        originalselfleft.rightchild = self
        originalselfleft.parent = originalparent
        if originalparent != None and originalself > originalparent:
            originalparent.rightchild = originalselfleft
        elif originalparent != None and originalself < originalparent:               
            originalparent.leftchild = originalselfleft
        if originalparent == None:
            tree.rootItem = self.parent
            return 1
                        
    def forcedrotateleft2(self, tree):
        '''Forced outward rotation to the left.'''
        originalself = self
        originalselfright = self.rightchild
        originalselfleft = self.leftchild
        originalselflpoint = self.leftpointer
        originalselfrpoint = self.rightpointer
        originalselfleftright = self.leftchild.rightchild
        originalselfleftleft = self.leftchild.leftchild
        originalparent = self.parent
        
        self.leftchild = originalselfleftright
        self.leftchild.parent = self
        originalselfleft.rightchild = self.leftchild.leftchild
        originalselfleft.rightpointer = self.leftchild.leftpointer
        self.leftchild.leftchild = originalselfleft
        self.leftchild.leftpointer = originalselflpoint
        self.leftchild.leftchild.parent = self.leftchild
        self.forcedrotateright(tree)                    
  
    def forcedrotateright2(self, tree):
        '''Forced outward rotation to right.'''
        originalself = self
        originalselfright = self.rightchild
        originalselfleft = self.leftchild
        originalselflpoint = self.leftpointer
        originalselfrpoint = self.rightpointer
        originalselfrightright = self.rightchild.rightchild
        originalselfrightleft = self.rightchild.leftchild
        originalparent = self.parent
        
        self.rightchild = originalselfrightleft
        self.rightchild.parent = self
        originalselfright.leftchild = self.rightchild.rightchild
        originalselfright.leftpointer = self.rightchild.rightpointer
        self.rightchild.rightchild = originalselfright
        self.rightchild.rightpointer = originalselfrpoint
        self.rightchild.rightchild.parent = self.rightchild
        self.forcedrotateleft(tree)
            
    def fix_rotation(self,tree):
        '''The method to reorder the tree entirely. Often used throughout the program. A combination of all the above forced rotations with checks to see if a rotation needs to be done or not.'''
        
        if self.leftpointer == 'red' and self.rightpointer == 'red':      # A four node cannot stay in a Red-Black Tree
            self.leftpointer = 'black'
            self.rightpointer = 'black'
            if self.parent != None and self.searchkey() < self.parent.searchkey():      #Fixes the splitsing of a 2-node parent.
                self.parent.leftpointer = 'red'
            elif self.parent != None and self.searchkey() > self.parent.searchkey():
                self.parent.rightpointer = 'red'
                
        if self.leftpointer == 'red' and self.leftchild.leftpointer == 'red':
    
            #Forced rotate right
            
            originalself = self
            originalselfright = self.rightchild
            originalselfleft = self.leftchild
            originalselflpoint = self.leftpointer
            originalselfrpoint = self.rightpointer
            originalselfleftright = self.leftchild.rightchild
            originalselfleftleft = self.leftchild.leftchild
            originalparent = self.parent

            self.leftchild = originalselfleftright
            if originalselfleftright != None:
                originalselfleftright.parent = self 
            self.leftpointer = originalselfleft.rightpointer
            self.parent = originalselfleft
            self.parent.rightpointer = originalselflpoint
            originalselfleft.rightchild = self
            originalselfleft.parent = originalparent
            if originalparent != None and originalself > originalparent:
                originalparent.rightchild = originalselfleft
            elif originalparent != None and originalself < originalparent:               
                originalparent.leftchild = originalselfleft
            if originalparent == None:
                tree.rootItem = self.parent
                
            self.parent.fix_rotation(tree)
            return 1
        elif self.rightpointer == 'red' and self.rightchild.rightpointer == 'red':

            #Forced rotate left
            
            originalself = self
            originalselfright = self.rightchild
            originalselfleft = self.leftchild
            originalselflpoint = self.leftpointer
            originalselfrpoint = self.rightpointer
            originalselfrightright = self.rightchild.rightchild
            originalselfrightleft = self.rightchild.leftchild
            originalparent = self.parent
    
            self.rightchild = originalselfrightleft
            if originalselfrightleft != None:
                originalselfrightleft.parent = self         
            self.rightpointer = originalselfright.leftpointer
            self.parent = originalselfright
            self.parent.leftpointer = originalselfrpoint            
            originalselfright.leftchild = self
            originalselfright.parent = originalparent  
            if originalparent != None and originalself > originalparent:
                originalparent.rightchild = originalselfright
            elif originalparent != None and originalself < originalparent:               
                originalparent.leftchild = originalselfright                
            if originalparent == None:
                tree.rootItem = self.parent
                            
            self.parent.fix_rotation(tree)
            return 1
        if self.leftpointer == 'red' and self.leftchild.rightpointer == 'red':
            
            #Forced rotate left 2, this rotation is the 'corner' shape that often happens at the third insert of an item in the redblacktree.
                        
            originalself = self
            originalselfright = self.rightchild
            originalselfleft = self.leftchild
            originalselflpoint = self.leftpointer
            originalselfrpoint = self.rightpointer
            originalselfleftright = self.leftchild.rightchild
            originalselfleftleft = self.leftchild.leftchild
            originalparent = self.parent
            
            self.leftchild = originalselfleftright
            self.leftchild.parent = self
            originalselfleft.rightchild = self.leftchild.leftchild
            originalselfleft.rightpointer = self.leftchild.leftpointer
            self.leftchild.leftchild = originalselfleft
            self.leftchild.leftpointer = originalselflpoint
            self.leftchild.leftchild.parent = self.leftchild
            
            self.fix_rotation(tree)
            
        if self.rightpointer == 'red' and self.rightchild.leftpointer == 'red':
        
            #Forced rotate right 2, this rotation is the 'corner' shape that often happens at the third insert of an item in the redblacktree.
            
            originalself = self
            originalselfright = self.rightchild
            originalselfleft = self.leftchild
            originalselflpoint = self.leftpointer
            originalselfrpoint = self.rightpointer
            originalselfrightright = self.rightchild.rightchild
            originalselfrightleft = self.rightchild.leftchild
            originalparent = self.parent
            
            self.rightchild = originalselfrightleft
            self.rightchild.parent = self
            originalselfright.leftchild = self.rightchild.rightchild
            originalselfright.leftpointer = self.rightchild.rightpointer
            self.rightchild.rightchild = originalselfright
            self.rightchild.rightpointer = originalselfrpoint
            self.rightchild.rightchild.parent = self.rightchild
            self.fix_rotation(tree)
                        
        return 0, None
