from math import floor, ceil, log
from random import shuffle

# array-based Heap implementation
# Because it is only used for heapsort, this class is defined here and not in ../structures/
class Heap:
    def __init__(self, a, attr):
        self.a = a
        self.attr = attr
    
    def parent(self, i):
        # if the ith element is the root, it will return a negative number
        return (i-1)//2
    
    def leftchild(self, i):
        c = (i*2)+1
        if c >= len(self.a):
            return -1
        return c
    
    def insert(self, el):
        self.a.append(el)
        i = len(self.a)-1
        
        # trickle up
        while self.parent(i) >= 0 and self.a[i].__dict__[self.attr] > self.a[self.parent(i)].__dict__[self.attr]:
            # swap
            self.a[i], self.a[self.parent(i)] = self.a[self.parent(i)], self.a[i]
            i = self.parent(i)
    
    def heapRebuild(self, root):
        child = self.leftchild(root)
        
        # no leftchild
        if child < 0 or child >= len(self.a):
            return
        
        rchild = child + 1
        # if rchild exists in self.a and it's bigger than the left child
        if rchild < len(self.a) and self.a[rchild].__dict__[self.attr] > self.a[child].__dict__[self.attr]:
            child = rchild
        
        # child is now the greatest possible child
        if self.a[root].__dict__[self.attr] < self.a[child].__dict__[self.attr]:
            # swap
            self.a[root], self.a[child] = self.a[child], self.a[root]
            self.heapRebuild(child)
    
    def delete(self, i):
        # swap i and last element
        last = len(self.a)-1
        self.a[last], self.a[i] = self.a[i], self.a[last]
        self.a.pop()
        self.heapRebuild(0)
    
            
    def __str__(self):
        s = ''
        h = self.height()
        for l in range(h+1):
            totalspaces = h*15 - 2**(l)
            spaces = ceil(totalspaces//((2**l)+1))*' '
            print('> spaces = ',len(spaces))
            print('> range = ',range(int(2**(l-1)),min(len(self.a), int(2**l))))
            for i in range(int(2**l-1),min(len(self.a), int(2**(l+1)-1))):
                s += spaces+"{0:02}".format(self.a[i])
            s += spaces+'|\n'  # newline
        
        return s
        
    def height(self):
        return ceil(log(len(self.a)+1, 2))
    
    

def heapsort(arr, attr):
    if len(arr) > 0:
        heap = Heap([arr[0]], attr)
        for el in arr[1:]:
            heap.insert(el)
        
        sortedarr = []
        
        while len(heap.a) > 0:
            sortedarr.insert(0, heap.a[0])  # prepend
            heap.delete(0)
        
        # seems to be the only way to replace the actual array
        for i in range(len(arr)):
            arr[i] = sortedarr[i]
        
        return arr
    else:
        return arr
