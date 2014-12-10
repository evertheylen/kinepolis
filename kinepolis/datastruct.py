import structures

def createDataStructure(T, attr):
    """ Creates a data structure of type T (or string, see below), where the elements 
    are ordered/searched for in attribute attr. """
    
    # We may specify the type with a string, but we have to use 'real' types
    # so we replace the string T with the type T (if it exists!)
    if type(T) == str:
        if T in structures.valid_names:
            T = structures.__dict__[T]
        else:
            print("%s is not a valid type."%T)
            return None
    
    return T(attr)

# Testing
"""
usarr = createDataStructure("UnsortedArray", "val")

class Test:
    def __init__(self, v):
        self.val = v

usarr.insert(Test(7))
usarr.insert(Test(8))

for i in usarr.inorder():
    print(i.val)

usarr.insert(Test(456))
usarr.delete(8)

for i in usarr.inorder():
    print(i.val)
"""