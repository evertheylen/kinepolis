# Author: Evert Heylen
# Date: 14-11-2014


class NotInBinTree(Exception):
    def __init__(self, value='requested element is not in BinTree'):
        self.value = value
    def __str__(self):
        return self.value


class BinTree:
    def __init__(self, root=None, parent=None,):
        self.root = root
        self.left = None
        self.right = None
        self.parent = parent
    
    
    def __str__(self):
        s = ''
        if self.root != None:
            s += "{0} [{1} {2}]".format(self.root, self.left, self.right)
        else:
            s = '/'
        return s
    
    
    def __repr__(self):
        return self.__str__()
    
    
    def retrieve(self, key):
        if self.root == None:
            return self, 'root'
        elif key < self.root:
            if self.left == None:
                return self, 'left'
            else:
                return self.left.retrieve(key)
        elif key > self.root:
            if self.right == None:
                return self, 'right'
            else:
                return self.right.retrieve(key)
        
        return self, 'root'
    
    
    def inorder_successor(self):
        if self.right == None:
            return None
        
        return self.right.mostleft()
    
    
    def inorder_predecessor(self):
        if self.left == None:
            return None
        
        return self.left.mostright()
    
    
    def mostleft(self):
        nextleftparent = self
        while nextleftparent.left != None:
            nextleftparent = nextleftparent.left
        
        return nextleftparent
    
    
    def mostright(self):
        nextrightparent = self
        while nextrightparent.right != None:
            nextrightparent = nextrightparent.right
        
        return nextrightparent
    
    
    def insert(self, item):
        tree, where = self.retrieve(item)
        
        # we won't insert a tree in the root
        if where != 'root':
            if tree.parent == None:
                parent = self
            else:
                parent = tree
            b = BinTree(item, parent)
            tree.__dict__[where] = b
        else:
            tree.root = item
        
    
    def delete(self, item):
        tree, where = self.retrieve(item)
        #print('tree=',tree,'treepar=',tree.parent,'where=',where)
        
        if where != 'root':
            raise NotInBinTree("can't delete a non-existing element")
        
        if tree.left == None and tree.right == None:
            if tree.parent == None:
                tree.root = None
            elif tree.parent.left != None and tree.parent.left.root == tree.root:
                tree.parent.left = None
            elif tree.parent.right != None and tree.parent.right.root == tree.root:
                tree.parent.right = None
            return
        
        # we can't delete it, must swap
        
        # swap with inorder_successor
        succ = tree.inorder_successor()
        if succ != None:
            #print('swapping',tree.root,'with',succ.root)
            tree.root, succ.root = succ.root, tree.root
            
            # Delete 
            succ.delete(succ.root)
            
            return
        
        # no inorder_successor, lets try with the inorder_predecessor
        pred = tree.inorder_predecessor()
        if pred != None:
            tree.root, pred.root = pred.root, tree.root
            
            # Delete 
            pred.delete(pred.root)
            
            return
    
    def inorder(self):
        if self.left != None:
            for i in self.left.inorder():
                yield i
        
        yield self.root
        
        if self.right != None:
            for i in self.right.inorder():
                yield i
    
    
    def postorder(self):
        if self.left != None:
            for i in self.left.postorder():
                yield i
        
        
        if self.right != None:
            for i in self.right.postorder():
                yield i
        
        yield self.root
    
    
    def preorder(self):
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
     
def main():
    b = BinTree()
    
    for i in [100,50,30,60,150,140,160]:
        b.insert(i)
    
    print(b)
    print('hoogte:',b.height())
    
    try:
        b.delete(55)
    except Exception as e:
        print('Voorspelde error:',e.value)
    
    # omdat inorder() een generator is, moeten we eerst de volledige lijst genereren
    # voor we kunnen verwijderen
    
    for i in [k for k in b.inorder()]:
        b.delete(i)
    
    print(b)
    print('hoogte:',b.height())
    
    import random
    
    arr = [i for i in range(20)]
    random.shuffle(arr)
    
    for i in arr:
        b.insert(i)
    
    c = BinTree()
    for i in b.preorder():
        c.insert(i)
    
    print(b)
    print(c)
    
    if str(b) == str(c):
        print('gelijk!')
    else:
        print('Error!')
    
    print('hoogte:',b.height())


if __name__=='__main__':
    main()