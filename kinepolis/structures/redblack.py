class Node:
    def __init__(self, attribute, item = None, next = None, precede = None, leftpointer = None, rightpointer = None, leftchild = None, rightchild = None, parent = None):
        self.item = item
        self.next = next
        self.precede = precede
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
        return self.searchkey() <= t2.searchkey()
        
    def __ge__(self, t2):
        return self.searchkey() >= t2.searchkey()
        
    def __lt__(self, t2):
        return self.searchkey() < t2.searchkey()
        
    def __gt__(self, t2):
        return self.searchkey() > t2.searchkey()
        
    def __repr__(self):
        if self.item != None:
            output = str(self.searchkey())
        else:
            return ('Empty node')
        if self.next != None:
            output += ', '+str(self.next)
        return output
        
    def insert(self, attribute, newItem, tree):
        tempNode = Node(attribute, newItem)
        if self.fix_rotation(tree) == 1:
            return self.parent.insert(newItem, tree)
        else:
            if newItem == self.item:
                self.treeItem = self.item
                return False
                
            if self.searchkey() == None:
                self.item = newItem
                return True
                
            elif self.leftchild == None and newItem.__dict__[attribute] < self.searchkey():
                if self.fix_rotation(tree) == 1:
                    self.insert(attribute, newItem, tree)
                self.leftchild = tempNode
                self.leftpointer = 'red'
                tempNode.parent = self
                tree.rootItem.fix_rotation(tree)
                return True
                
            elif self.rightchild == None and newItem.__dict__[attribute] > self.searchkey():
                if self.fix_rotation(tree) == 1:
                    self.insert(attribute, newItem, tree)        
                self.rightchild = tempNode
                self.rightpointer = 'red'
                tempNode.parent = self
                tree.rootItem.fix_rotation(tree)          
                return True  
                    
            else:
                if newItem.__dict__[attribute] < self.searchkey():
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
        '''The inorderTraversal is just a recursive algorithm. It #prints out the left most subtree of a tree, then the root and then the rightmost subtree. If we do that. The tree is #printed out in order.'''
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
        treeItem = self.find_searchKey(searchKey)
        if treeItem != None:    
            return True, treeItem.item
        else:
            return False, treeItem
                
    def find_searchKey(self, searchKey, delete=0):
        '''This function is used to find the location of an item in the tree. If delete = 1, all the nodes are transformed to a 3 or 4 node on the way to the item.'''
        if searchKey == self.searchkey():
            itemLocation = self
            return itemLocation
        
        elif self.leftchild == None and searchKey < self.searchkey():
            return None
            
        elif self.rightchild == None and searchKey > self.searchkey():
            return None   
        
        else:
            if delete == 1:
                '''if self.parent != None:
                    self.fix_nodes()'''
                if searchKey < self.searchkey():
                    return self.leftchild.find_searchKey(searchKey,1)
                else:
                    return self.rightchild.find_searchKey(searchKey,1)
            else:
                if searchKey < self.searchkey():
                    return self.leftchild.find_searchKey(searchKey)
                else:
                    return self.rightchild.find_searchKey(searchKey)
                    
    def find_successor(self, successorlist):   
        if self.item != None and self.leftchild == None and self.rightchild == None:
            successorlist.append(self)
        else:
            if self.leftchild != None:
                self.leftchild.find_successor(successorlist)
            successorlist.append(self)
            if self.rightchild != None:
                self.rightchild.find_successor(successorlist)        
    
    def fix_nodes(self):    
        '''Fixes that all nodes on the way to a node that has to be deleted are 3 or 4 nodes.'''
        if self.leftpointer == 'black' and self.rightpointer == 'black':
            # self is a 2 node
            if self.item < self.parent.item and self.parent.leftpointer != 'red':
                # self is not in the same node as its parent (and thus is not a 3 node)
                self.leftpointer = 'red'
                self.rightpointer = 'red'
            elif self.item > self.parent.item and self.parent.rightpointer != 'red':
                self.leftpointer = 'red'
                self.rightpointer = 'red'
    
    def fixdoubleblack(self, tree):
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
        itemLocation = self.find_searchKey(searchKey,1)     #Zoek de knoop n die het te verwijderen item bevat en vorm alle knopen op het pad om tot een 3 of 4 knoop.
        if itemLocation == None:
            return False
        successorlist = []
        self.find_successor(successorlist)          #The inorder successor is the item zo dat self < inordersuccessor and self >= alles dat < inorder successor            
        successor = None
        for i in range(len(sorted(successorlist))-1):       #Zoek de successor van het item en vorm alle knopen op het pad om tot een 3 of 4 knoop.
            if sorted(successorlist)[i].searchkey() == searchKey:
                successor = sorted(successorlist)[i+1]
        if successor == None:
            successor = sorted(successorlist)[-1]
        successorLocation = self.find_searchKey(successor.searchkey(),1)
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
                    itemLocation.item = None
                    itemLocation.parent.leftpointer = 'blackblack'
                    itemLocation.fixdoubleblack(tree)
                elif itemLocation > itemLocation.parent and itemLocation.parent.rightpointer == 'black':
                    itemLocation.item = None
                    itemLocation.parent.rightpointer = 'blackblack'
                    itemLocation.fixdoubleblack(tree)
                   
            else:
                tree.rootItem = Node(None, None)
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
            successorLocation_originalparent = successor.parent                 
            tempItem = successor                           #Swap het item en zijn successor
            successorLocation = itemLocation
            itemLocation = tempItem
            if successorLocation.parent != None:
                if itemLocation.searchkey() < successorLocation_originalparent.searchkey() and successorLocation.parent.leftpointer == 'red':
                    successorLocation.parent.leftchild = None
                    successorLocation.parent.leftpointer = None
                elif itemLocation.searchkey() > successorLocation_originalparent.searchkey() and successorLocation.parent.rightpointer == 'red':  
                    successorLocation.parent.rightchild = None
                    successorLocation.parent.rightpointer = None
                    
                elif successorLocation.leftchild != None and successorLocation.rightchild == None:
                    if successorLocation.parent == None:
                        tree.rootItem = successorLocation.leftchild
                        successorLocation.leftchild.parent = None
                    else:
                        if itemLocation.item < successorLocation_originalparent:
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
                        if itemLocation.item < successorLocation_originalparent:
                            successorLocation.parent.leftchild = successorLocation.rightchild
                            successorLocation.rightchild.parent = successorLocation.parent
                            successorLocation.parent.leftpointer = 'black'
                        else:
                            successorLocation.parent.rightchild = successorLocation.rightchild
                            successorLocation.rightchild.parent = successorLocation.parent
                            successorLocation.parent.rightpointer = 'black'
                      
                else:
                    #If the in-order successor is a black leaf.
                    
                    if itemLocation.item < successorLocation_originalparent and successorLocation.parent.leftpointer == 'black':
                        successorLocation.item = None
                        successorLocation.parent.leftpointer = 'blackblack'
                        successorLocation.fixdoubleblack(tree)
                    elif itemLocation.item > successorLocation_originalparent and successorLocation.parent.rightpointer == 'black':
                        successorLocation.item = None
                        successorLocation.parent.rightpointer = 'blackblack'
                        successorLocation.fixdoubleblack(tree)             

    def forcedrotateleft(self, tree):
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
            originalselfrightleft.parent = self         #!!!!!!!!!!!!!!!!!!!!!!!
        self.rightpointer = originalselfright.leftpointer
        self.parent = originalselfright
        self.parent.leftpointer = originalselfrpoint            
        self.parent.leftchild = self
        self.parent.parent = originalparent  
        if originalparent != None and originalself > originalparent:
            originalparent.rightchild = originalselfright
        elif originalparent != None and originalself < originalparent:               
            originalparent.leftchild = originalselfright                
        if originalparent == None:
            tree.rootItem = self.parent
            return 1
            
    
    def forcedrotateright(self, tree):       
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
            originalselfleftright.parent = self #!!!!!!!!!!!!!!!!!!!!!!!
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
        
        if self.leftpointer == 'red' and self.rightpointer == 'red':
            self.leftpointer = 'black'
            self.rightpointer = 'black'
            if self.parent != None and self.searchkey() < self.parent.searchkey():      #Fixes the splitsing of a 2-node parent.
                self.parent.leftpointer = 'red'
            elif self.parent != None and self.searchkey() > self.parent.searchkey():
                self.parent.rightpointer = 'red'
                
        if self.leftpointer == 'red' and self.leftchild.leftpointer == 'red':
    
            #Werkende rotatie naar rechts langs binnen
            
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
                originalselfleftright.parent = self #!!!!!!!!!!!!!!!!!!!!!!!'''
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

            #Werkende rotatie naar links langs binnen
            
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
                originalselfrightleft.parent = self         #!!!!!!!!!!!!!!!!!!!!!!!'''
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
            
            #Werkende rotatie langs buiten naar links die dikwijls aan het begin voorkomt, namelijk het "hoekje", nadat 3 elementen zijn geinsert.
                        
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
        
            #Werkende rotatie langs buiten naar rechts die dikwijls aan het begin voorkomt, namelijk het "hoekje", nadat 3 elementen zijn geinsert.
            
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
        
class RedBlackTree:
    def __init__(self, attribute, rootItem = None):
        self.rootItem = Node(attribute, rootItem)
        self.attribute = attribute
        
    def isEmpty(self):
        if self.rootItem.searchkey() == None:
            return True
        else:
            return False
        
    def insert(self, newItem):
        return self.rootItem.insert(self.attribute, newItem, self) 
        
        
    def inorder(self, visit = None):
        return self.rootItem.inorderTraversal(visit)
    
    def retrieve(self, searchKey):
        (success, value) = self.rootItem.retrieve(searchKey)
        return value
        
    def delete(self, searchKey):
        return self.rootItem.delete(searchKey, self)
        
'''boom = Red_BlackTree()
boom.insert(10)
boom.insert(100)
boom.insert(30)
boom.insert(80)
boom.insert(50)
print(boom.rootItem)
boom.inorderTraversal()
boom.delete(10)
print(boom.rootItem)
boom.insert(60)
print(boom.rootItem)
boom.inorderTraversal()
boom.insert(70)
boom.inorderTraversal()
boom.insert(40)
boom.inorderTraversal()
boom.delete(80)
boom.inorderTraversal()
boom.insert(90)
boom.insert(20)
boom.inorderTraversal()
boom.delete(30)
boom.inorderTraversal()
boom.delete(70)
boom.inorderTraversal()'''


