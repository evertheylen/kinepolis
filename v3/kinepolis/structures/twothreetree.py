
# Author: Evert Heylen
# Dit is een 2-3 boom implementatie die ik vandaag (13-01-2015) op een namiddag nog in elkaar heb gestoken.
# Alles werkt, behalve delete. Daarvoor gebruik ik een klein truckje, wat zeer inefficient is.
# In tegenstelling tot de 2-3 boom van Anthony, werkt deze wel met de rest van het systeem.



def searchValues(values, attr, key):
    for v in values:
        if v.__dict__[attr] == key:
            return v
    return None

def searchIndex(values, attr, key):
    for i, v in enumerate(values):
        if v.__dict__[attr] == key:
            return i
    return None

def setOtherParent(nodelist, newparent):
    for n, _ in enumerate(nodelist):
        nodelist[n].parent = newparent
    return nodelist

class Node:
    def __init__(self, attr, parent=None, values=[], children=[]):
        self.attr = attr
        self.parent = parent
        self.values = values
        self.children = children
    
    def _key(self, el):
        return el.__dict__[self.attr]
    
    def size(self):
        return len(self.children)  # 0, 2 or 3
    
    def findNode(self, key):
        if key in [self._key(v) for v in self.values]:
            return self
        else:
            if len(self.children) == 2:
                if key < self._key(self.values[0]):
                    return self.children[0].findNode(key)
                else:
                    return self.children[1].findNode(key)
            elif len(self.children) == 3:
                if key < self._key(self.values[0]):
                    return self.children[0].findNode(key)
                elif self._key(self.values[0]) < key < self._key(self.values[1]):
                    return self.children[1].findNode(key)
                else:
                    return self.children[2].findNode(key)
            else:
                # leaf
                return self
    
    def retrieve(self, key):
        return searchValues(self.findNode(key).values, self.attr, key)
    
    
    def insert(self, el):
        if self.isEmpty():
            self.values = [el]
            #print("no fixing")
            return True
        
        key = self._key(el)
        
        if len(self.children) == 0:
            # we have reached the node in which searching would stop
            self._append(el)
            
            # balance the tree!
            self._balanceAfterInsert()
        else:
            # recursively call until the node where searching would stop is found
            node = self.findNode(key)
            if node != None:
                return node.insert(el)
            else:
                #print("node is none...")
                return False
    
    def _append(self, el):
        """Append in the right place in el"""
        
        key = self._key(el)
        
        if len(self.values) == 0:
            self.values = [el]
        elif len(self.values) == 1:
            if key < self._key(self.values[0]):
                self.values = [el] + self.values
            else:
                self.values = self.values + [el]
        elif len(self.values) == 2:
            if key < self._key(self.values[0]):
                self.values = [el] + self.values
            elif self._key(self.values[0]) < key < self._key(self.values[1]):
                self.values = [self.values[0], el, self.values[1]]
            else:
                self.values = self.values + [el]
        else:
            #print("catastrophic error, we're all going to die.........   while _appending "+str(el))
            pass
        #print("     ",self)
    
    def _childIndex(self, key):
        """Pick the right childIndex based on the key.
        Very similar to _append, but for children.
        Assumes that self is a goodNode."""
        
        if len(self.values) == 1:
            if key < self._key(self.values[0]):
                return 0
            else:
                return 1
        elif len(self.values) == 2:
            if key < self._key(self.values[0]):
                return 0
            elif self._key(self.values[0]) < key < self._key(self.values[1]):
                return 1
            else:
                return 2
        elif len(self.values) == 3:
            if key < self._key(self.values[0]):
                return 0
            elif self._key(self.values[0]) < key < self._key(self.values[1]):
                return 1
            elif self._key(self.values[1]) < key < self._key(self.values[2]):
                return 2
            else:
                return 3
        else:
            #print("no children.........   while _child'ing "+str(key), len(self.values))
            pass
        
    def _leaf(self):
        return len(self.children) == 0
    
    def _addChild(self, node):
        childIndex = self._childIndex(self._key(node.values[0])) # ?
        if childIndex != None:
            #print(childIndex)
            if childIndex >= len(self.children):
                self.children.append(node)  # real list append, not _append
            else:
                self.children = self.children[:childIndex] + [node] + self.children[childIndex:]
        else:
            # assume that more children will be added further in the process
            self._createChildren()
            self.children[0] = node
            #print("WHADAFUUUCK",self, node)
    
    def _removeChild(self, child):
        self.children.remove(child)
        # I hope this works
    
    def _balanceAfterInsert(self):
        """the node where there is an extra value (too much) is self."""
        #print("fixing insert", self.isGoodNode())
        
        if self.isGoodNode():
            return  # nothing to fix
        
        # first, if the node is a leaf (and it's not the root), we'll push the middle element up
        # and then recursively call the _fixInsert on the parent.
        if self._leaf() and self.parent != None:
            #print(">>> leaf")
            # insert middle value in parent
            
            #print("self:",self)
            
            #print("parent:",self.parent)
            self.parent._append(self.values[1])
            #print("parent after append:",self.parent)
            
            # now, split this node up in two
            # first, uncouple parent with this node
            self.parent._removeChild(self)
            #print("parent after remove child:",self.parent)
            
            # then, split the node
            self.parent._addChild(Node(self.attr, self.parent, [self.values[0]]))
            #print("parent after split:",self.parent)
            self.parent._addChild(Node(self.attr, self.parent, [self.values[2]]))
            #print("parent after split2:",self.parent)
            
            # now fix the parent
            self.parent._balanceAfterInsert()
            #print("parent after balance",self.parent)
        # if the node is an internal node (or root)
        else:
            if self.parent == None:
                #print(">>> root")
                # root
                # self will remain root, but we'll change all the rest
                # mind you, we need to change the parents of the children of left- and rightchild
                leftchild = Node(self.attr, self, values=[self.values[0]])
                leftchild.children = setOtherParent(self.children[:2], leftchild)
                rightchild = Node(self.attr, self, values=[self.values[2]])
                rightchild.children = setOtherParent(self.children[2:], rightchild)
                self.values = [self.values[1]]
                self.children = [leftchild, rightchild]
                # this will make the tree grow in height
                # no need for recursive call
            else:
                #print(">>> internal")
                # internal node
                # simply push middle element upward
                #print("parent:",self.parent)
                self.parent._append(self.values[1])
                #print("parent after append:",self.parent)
                
                # and split
                firstchild = Node(self.attr, self.parent, values=[self.values[0]])
                firstchild.children = setOtherParent(self.children[:2], firstchild)
                secondchild = Node(self.attr, self.parent, values=[self.values[2]])
                secondchild.children = setOtherParent(self.children[2:], secondchild)
                # remove self from parent's children
                self.parent._removeChild(self)
                # and add the splitted children (this will make the tree forget about self)
                self.parent._addChild(firstchild)
                self.parent._addChild(secondchild)
                
                self.parent._balanceAfterInsert()
                # and balance again...
    
    
    def delete(self, key):
        node = self.findNode(key)
        index = searchIndex(node.values, self.attr, key)
        
        if not node._leaf():
            # first swap with inorder successor
            #print("index",index)
            #print("node to swap with",node.children[index+1]._mostLeft())
            #print(locals())
            #print("value before swapping",node.values[index])
            node.values[index], node.children[index+1]._mostLeft().values[0] = node._inorderSuccesor(index), node.values[index]
            #print("value after swapping",node.values[index])
            node = node.children[index+1]._mostLeft()
            #print("new node",node)
            index = 0
            
        # if the node is a leaf, we don't need to swap.
        # just remove
        node.values.remove(searchValues(node.values, self.attr, key))
        # and balance again (not really balance, but you get the idea)
        node._balanceAfterDelete()
            
    
    def _inorderSuccesor(self, index):
        # only call when you are sure that self isn't a leaf.
        return self.children[index+1]._mostLeft().values[0]
    
    def _mostLeft(self):
        left = self.children[0] if len(self.children) >= 1 else self
        prev = left
        while left != None:
            prev = left
            left = left.children[0] if len(left.children) >= 1 else None
        return prev
    
    def _balanceAfterDelete(self):
        if self.isEmpty():
            # only do stuff when self is empty
            if self.parent == None:  # root
                # replace self with self.children[0]
                newroot = self.children[0]
                self.values = newroot.values
                self.children = newroot.children
                for childindex, _ in enumerate(self.children):
                    self.children[childindex].parent = self
                    
            else: # not root...
                # het lege blad heeft een aangrenzende sibling met 2 elementen -> herverdelen
                siblings = self.parent.children
                siblings.remove(self)
                
                allvalues = []
                for i in range(len(self.parent.values)):
                    if self.parent.children[i] in siblings:
                        allvalues.extend(self.parent.children[i].values)  # add all values from that child to allvalues
                    allvalues.append(self.parent.values[i])
                # add most right child's values
                #print("values",self.parent.values)
                #print("children", self.parent.children)
                if len(self.parent.values) < len(self.parent.children) and self.parent.children[len(self.parent.values)] in siblings:
                    allvalues.extend(self.parent.children[len(self.parent.values)].values)
                
                # at this point, allvalues contains all the values, from parent and siblings.
                newNode = Node(self.attr, None)
                
                for val in allvalues:
                    newNode.insert(val)
                
                if self.parent.parent == None:
                    # replace root
                    # ...
                    #print("Oh no please no")
                    pass
                else:
                    childindex = 0
                    for i, child in enumerate(self.parent.parent.children):
                        if child == self.parent:
                            childindex = i
                    
                    newNode.parent = self.parent.parent
                    self.parent.parent.children[childindex] = newNode
                    #print("nn",newNode)
                    
                    # ...
                    
                # het lege blad heeft enkel aangrenzende siblings met 1 element -> samenvoegen
                
                # bij samenvoegen: recursief
    
    def _createChildren(self):
        """Creates children (all None) based on current values"""
        self.children = [None] * (len(self.values)+1)
            
    def split(self):
        pass
    
    def isEmpty(self):
        return len(self.values) == 0
    
    def isGoodNode(self):
        # the node is good if it only contains maximum 2 values and 3 children
        # and some more rules...
        if len(self.values) == 0 and self.parent == None:
            return True  # empty root Node
        elif 0 < len(self.values) <= 2 and (len(self.children) == 0 or len(self.children) == len(self.values)+1):
            return True
        
        # not one of the nodes above, so it must be wrong
        #print("not good node", self)
        return False
    
    
    def inorder(self):
        if not self.isEmpty():
            for i in range(len(self.values)): # yield children[0], values[0], children[1], values[1]
                if i < len(self.children) and self.children[i] != None:
                    yield from self.children[i].inorder()
                yield self.values[i]
                
            if len(self.children) != 0 and self.children[len(self.children)-1] != None:
                    yield from self.children[len(self.children)-1].inorder() # yield most right children

    
    def __str__(self):
        return " {} ({})".format("  ".join([str(v) for v in self.values]), " ".join([str(c) for c in self.children]))
    
    __repr__ = __str__


import sorting

class TwoThreeTree:
    def __init__(self, attribute):
        self.root = Node(attribute)
        self._attribute = attribute

    def attribute(self):
        return self._attribute

    def insert(self, el):
        if self.attribute() not in el.__dict__.keys():
            # print("Wrong type!")
            return False
            
        if el in list(self.inorder()):
            return False  # not unique!

        self.root.insert(el)
        return True

    def retrieve(self, key):
        # simple sequential search
        return self.root.retrieve(key)

    def delete(self, key):
        # not implemented so...
        array = list(self.root.inorder())
        goodarray = []
        for i in array:
            if i.__dict__[self.attribute()] != key:
                goodarray.append(i)
        
        if set(goodarray) == set(array):
            return False # noting to delete
        
        self.root = Node(self.attribute())
        for i in goodarray:
            self.root.insert(i)
        
        return True

    def isEmpty(self):
        return self.root.isEmpty()

    def sort(self, attr, sortFunc = sorting.bubblesort):
        if attr == self.attribute():
            yield from self.inorder()
        else:
            array = list(self.inorder())
            array = sortFunc(array, attr)
            
            for i in array:
                yield i

    def inorder(self):
        yield from self.root.inorder()


"""
# testing...

class Page:
    def __init__(self, nr, text):
        self.nr = nr
        self.text = text
        
    def __repr__(self):
        return str(self.nr)
        #return "[{}: {}]".format(self.nr, self.text)

p = {
    1: Page(1, "een"),
    2: Page(2, "twee"),
    3: Page(3, "drie"),
    4: Page(4, "vier"),
    5: Page(5, "vijf")
    }

def main():
    '''
    n = Node('nr', values=[p[2]], children=[Node('nr', None, values=[p[1]]), Node('nr', None, values=[p[3]])])
    print(list(n.inorder()))
    print(n.retrieve(2))
    # '''
    l = [50, 30, 10, 20, 40, 70, 90, 60, 80, 100, 39, 38, 37, 36, 35, 34, 33, 32]
    
    fancyp = [Page(i, "") for i in l]

    n = Node('nr')
    
    for i in fancyp:
        n.insert(i)
        print("---------------\n",n)
        print("\n\n")
        #print(i)
        
    print("\n\n\n")
    print(n)
    insertingWorks = str(n) == ' 37 ( 33 ( 30 ( 10  20 ()  32 ())  35 ( 34 ()  36 ()))  50 ( 39 ( 38 ()  40 ())  70  90 ( 60 ()  80 ()  100 ())))'
    print(n.parent)
    
    # DELETION ---------------------
    
    n.insert(Page(36.5, ""))
    print(n)
    
    print(n._inorderSuccesor(0))
    
    m = [20, 35, 100, 50, 37]
    
    for i in m[:4]: #m[:2]:
        n.delete(i)
        print("----delete %d -----------\n"%i,n)
        print("\n\n")
        
    print(n)
    
    
    n = Node('nr')
    n.insert(p[1])
    print('')

    n.insert(p[3])
    print('')

    n.insert(p[2])
    print('')

    n.insert(p[5])
    print("\n")


    print(n)
    
    
    
    print("Inserting works?",insertingWorks)

if __name__=='__main__':
    main()
"""