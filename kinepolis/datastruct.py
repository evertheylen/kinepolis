import structures
# imports all Table-like structures

from structures.queue import Queue
from structures.stack import Stack
# imports the simple datastructs like heap and stack.
# these are separate classes, and can not be used with createDataStructure().

def createDataStructure(T, attr='ID', **kwargs):
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
    
    return T(attr, **kwargs)
