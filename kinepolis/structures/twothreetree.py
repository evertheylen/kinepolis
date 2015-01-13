





def searchValues(values, attr, key):
    for v in values:
        if v.__dict__[attr] == key:
            return v
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
        return searchValues(self.findNode(key), self.attr, key)
    
    
    def insert(self, el):
        if self.isEmpty():
            self.values = [el]
            print("no fixing")
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
                print("node is none...")
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
            print("catastrophic error, we're all going to die.........   while _appending "+str(el))
        
        print("     ",self)
    
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
            print("no children.........   while _child'ing "+str(key), len(self.values))
    
    def _leaf(self):
        return len(self.children) == 0
    
    def _addChild(self, node):
        childIndex = self._childIndex(self._key(node.values[0])) # ?
        if childIndex != None:
            print(childIndex)
            if childIndex >= len(self.children):
                self.children.append(node)  # real list append, not _append
            else:
                self.children = self.children[:childIndex] + [node] + self.children[childIndex:]
        else:
            # assume that more children will be added further in the process
            self._createChildren()
            self.children[0] = node
            print("WHADAFUUUCK",self, node)
    
    def _removeChild(self, child):
        self.children.remove(child)
        # I hope this works
    
    def _balanceAfterInsert(self):
        """the node where there is an extra value (too much) is self."""
        print("fixing insert", self.isGoodNode())
        
        if self.isGoodNode():
            return  # nothing to fix
        
        # first, if the node is a leaf (and it's not the root), we'll push the middle element up
        # and then recursively call the _fixInsert on the parent.
        if self._leaf() and self.parent != None:
            print(">>> leaf")
            # insert middle value in parent
            
            print("self:",self)
            
            print("parent:",self.parent)
            self.parent._append(self.values[1])
            print("parent after append:",self.parent)
            
            # now, split this node up in two
            # first, uncouple parent with this node
            self.parent._removeChild(self)
            print("parent after remove child:",self.parent)
            
            # then, split the node
            self.parent._addChild(Node(self.attr, self.parent, [self.values[0]]))
            print("parent after split:",self.parent)
            self.parent._addChild(Node(self.attr, self.parent, [self.values[2]]))
            print("parent after split2:",self.parent)
            
            # now fix the parent
            self.parent._balanceAfterInsert()
            print("parent after balance",self.parent)
        # if the node is an internal node (or root)
        else:
            if self.parent == None:
                print(">>> root")
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
                print(">>> internal")
                # internal node
                # simply push middle element upward
                print("parent:",self.parent)
                self.parent._append(self.values[1])
                print("parent after append:",self.parent)
                
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
        if node == None:
            return False
        else:
            node.values.remove(searchValues(node.values, self.attr, key))
            node._balanceAfterDelete()
            return True
    
    def _balanceAfterDelete(self):
        print("fixing delete")
    
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
        print("not good node", self)
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
    
    fancyp = [Page(i, "") for i in [50, 30, 10, 20, 40, 70, 90, 60, 80, 100, 39, 38, 37, 36, 35, 34, 33, 32][:20]]

    n = Node('nr')
    
    for i in fancyp:
        n.insert(i)
        print("---------------\n",n)
        print("\n\n")
        #print(i)
        
    print("\n\n\n")
    print(n)
    print(n.parent)
    
    """
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
    
    # """

if __name__=='__main__':
    main()
    