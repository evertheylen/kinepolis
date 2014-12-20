
from structures.bintree import BinTree

def treesort(arr, attr):
    if len(arr) == 0:
        return arr
    
    b = BinTree(attr)
    
    for el in arr:
        b.insert(el)
    
    sarr = list(b.inorder())
    # replace the actual array
    for i in range(len(arr)):
        arr[i] = sarr[i]
    return arr
