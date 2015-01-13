
class BinTree:
    def __init__(self, attr, root=None, parent=None):
        self.root = root
        self.left = None
        self.right = None
        self.parent = parent
        self._attribute = attr
    
    
    def attribute(self):
        return self._attribute
    
    def _key(self, el):
        return el.__dict__[self.attribute()]
    
    def _retrieve(self, key):
        if self.root == None:
            return self, 'root'
        elif key < self._key(self.root):
            if self.left == None:
                return self, 'left'
            else:
                return self.left._retrieve(key)
        elif key > self._key(self.root):
            if self.right == None:
                return self, 'right'
            else:
                return self.right._retrieve(key)
        
        return self, 'root'
    
    def retrieve(self, key):
        tree, where = self._retrieve(key)
        if where == 'root':
            return tree.root
        return None
    
    
    def _inorder_successor(self):
        if self.right == None:
            return None
        
        return self.right._mostleft()
    
    
    def _inorder_predecessor(self):
        if self.left == None:
            return None
        
        return self.left._mostright()
    
    
    def _mostleft(self):
        nextleftparent = self
        while nextleftparent.left != None:
            nextleftparent = nextleftparent.left
        
        return nextleftparent
    
    
    def _mostright(self):
        nextrightparent = self
        while nextrightparent.right != None:
            nextrightparent = nextrightparent.right
        
        return nextrightparent
    
    
    def insert(self, item):
        tree, where = self._retrieve(self._key(item))
        
        # just insert if tree is empty
        if self.isEmpty():
            self.root = item
            return True
        
        # we won't insert a tree in the root
        if where != 'root':
            if tree.parent == None:
                parent = self
            else:
                parent = tree
            b = BinTree(self.attribute(), item, parent)
            tree.__dict__[where] = b
            return True
        
        # returning False if the element is already in the datastructure
        return False
        
    
    def delete(self, key):
        if self.isEmpty():
            return False
        
        tree, where = self._retrieve(key)
        #print('tree=',tree,'treepar=',tree.parent,'where=',where)
        
        if where != 'root':
            #raise NotInBinTree("can't delete a non-existing element")
            return False
        if tree.left == None and tree.right == None:
            if tree.parent == None:
                tree.root = None
            elif tree.parent.left != None and tree.parent.left.root == tree.root:
                tree.parent.left = None
            elif tree.parent.right != None and tree.parent.right.root == tree.root:
                tree.parent.right = None
            return True
        
        # we can't delete it, must swap
        
        # swap with inorder_successor
        succ = tree._inorder_successor()
        if succ != None:
            #print('swapping',tree.root,'with',succ.root)
            tree.root, succ.root = succ.root, tree.root
            
            # Delete 
            succ.delete(self._key(succ.root))
            
            return True
        
        # no inorder_successor, lets try with the inorder_predecessor
        pred = tree._inorder_predecessor()
        if pred != None:
            tree.root, pred.root = pred.root, tree.root
            
            # Delete 
            pred.delete(self._key(pred.root))
            
            return True
    
    def sort(self, attr, sortFunc=None):
        # prevent circular depencies
        from sorting import bubblesort
        if sortFunc == None:
            sortFunc = bubblesort
        
        if attr == self.attribute():
            yield from self.inorder()
        else:
            templist = list(self.inorder())
            sortFunc(templist, attr)
            for i in templist:
                yield i
            
    
    def inorder(self):
        if self.left != None:
            for i in self.left.inorder():
                yield i
        
        if self.root != None:
            yield self.root
        
        if self.right != None:
            for i in self.right.inorder():
                yield i
    
    def isEmpty(self):
        for i in self.inorder():
            return False
        return True
    
    def postorder(self):
        if self.left != None:
            for i in self.left.postorder():
                yield i
        
        
        if self.right != None:
            for i in self.right.postorder():
                yield i
        
        if self.root != None:
            yield self.root
    
    
    def preorder(self):
        if self.root != None:
            yield self.root
        
        if self.left != None:
            for i in self.left.preorder():
                yield i
        
        if self.right != None:
            for i in self.right.preorder():
                yield i
     
     
    def height(self):
        if self.root == None:
            return 0
        if self.left == None and self.right == None:
            return 1
        if self.left != None and self.right == None:
            return 1+self.left.height()
        if self.left == None and self.right != None:
            return 1+self.right.height()
        return 1 + max(self.left.height(), self.right.height())
    
    def __str__(self):
        s = ''
        if self.root != None:
            s += "{0} [{1} {2}]".format(self.root, self.left, self.right)
        else:
            s = '/'
        return s
    
    
    def __repr__(self):
        return "BinTree: "+self.__str__()

