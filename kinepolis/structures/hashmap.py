# Author: Evert Heylen
# Testcode door: Stijn Janssens


# As an example, we can use the (unsorted) linked chain
from structures.uslinkedchain import USLinkedChain

import sorting

def lineairProbing(x):
    return x

def quadraticProbing(x):
    return x**2


def createModFunc(mod):
    return lambda x: x % mod



# -----------------------------------
# Some documentation:
#
# When inserting, the class of the objects inserted should implement the function .__dict__[self._attribute].
# The function .__dict__[self._attribute] should be of type A, so that type A:
#    - is convertible to an int (__int__ must be implemented)
#    - can be used with the '==' operator (__eq__ must be implemented)
#
# When searching for or deleting based on a searchkey, that searchkey should be UNIQUE, and it
# should be of type A mentioned above. If we're looking for object B with searchkey C, the
# following should be true:
#     B.__dict__[self._attribute] == C
# 
# If you want to chain, you should offer some class as the chaining class. It should be a class
# created with createDataStructure in datastruct.py.
# 
# The hashFunc/addressFunc should both be methods that take an integer and return
# an integer.
#
# You can't (or rather, you shouldn't) change the way of addressing while the
# hashmap contains data. Therefore, there is no function changeOpenAddressing.
# If you really want to switch to another addressing way, you need to create a
# new hashmap, something like this:
#   newhashmap = Hashmap( <new parameters, including new way of addressing> )
#   for element in oldhashmap.hashMapInorderTraversal():
#       newhashmap.hashMapInsert(element)
# newhashmap will then contain the same data, while using another way of addressing.
#

class Deleted:
    """ Meaning: this was once an element with key self.key """
    
    def __init__(self, key):
        self.key == key
    
    def __eq__(self, other):
        if self.key == other.key:
            return True
        return False


class Hashmap:
    def __init__(self, attr, length=21, hashFunc=None, collisionSolution = USLinkedChain, toInt = int):
        # chaining is a class, hashFunc and addressFunc are both functions.
        # If chaining is None, we don't chain.
        # If addressFunc is None, we will utilize the chaining method.
        # If they are both not None, we will utilize the chaining method
        
        # For example, if you want to create a hashmap with quadraticProbing,
        # length 51 and the default mod function, you write:
        #    hm = Hashmap(51, None, quadraticProbing)
        
        # If you want to create a hashmap with Linkedchain chaining, you write:
        #    hm = Hashmap(23, None, None, Linkedchain)
        
        self._attribute = attr
        self._array = [None]*length
        self._length = length
        
        if type(collisionSolution) == type:
            self._chaining = collisionSolution  # chaining class
            self._addressFunc = None
        else:
            self._chaining = None
            self._addressFunc = collisionSolution
                # function to calculate next address, be it by probing or double hashing
        
        # Default hashFunc
        if hashFunc == None:
            hashFunc = createModFunc(self._length)
        
        # The hashing function.
        self._hashFunc = hashFunc
        
        # The function that translates stuff to an int, default is just the int function.
        self._toInt = toInt
    
    
    def attribute(self):
        return self._attribute
    
    def _key(self, element):
        return element.__dict__[self.attribute()]
    
    def _locationOf(self, key):
        """ Private function to calculate the location in the array of some element.
        Note that the element does not need to be in the array. """
        
        location = self._hashFunc(self._toInt(key))
        origloc = location
        
        if self._chaining == None:  # probing
            #checked = [False] * self._length
            i = 1
            reached = False
            while i <= self._length:    # simple solution to prevent looping
                # stop looping when:
                #   - the current element is None
                #   - the current element is Deleted, with the right key
                #   - the element is found
                if self._array[location] == None \
                    or (type(self._array[location]) == Deleted and self._array[location].key == key) \
                    or self._key(self._array[location]) == key:
                    
                    reached = True
                    break
                
                location = origloc + self._addressFunc(i)
                
                # modulo location, so that it'll never reach an index not in our array
                location = location % self._length
                i+=1
            
            # If we have reached the right element...
            if reached:
                return location
            else:
                return -1
        
        else:  # chaining
            return location
    
    
    def insert(self, el):
        location = self._locationOf(self._key(el))
            
        if self._chaining == None:  # we use probing
            if location == -1:
                return False
            
            # if the location isn't -1; we can just insert
            self._array[location] = el
            return True
        
        else:  # we use chaining
            if self._array[location] == None:
                # Create a new instance of the desired chaining class, with the same attribute
                self._array[location] = self._chaining(self.attribute())
                return self._array[location].insert(el)
                # el should have a method .__dict__[self._attribute], because reusing the int()
                # functionality will also be problematic for the chaining, as it
                # will have the same issues as the hashmap. .__dict__[self._attribute] should
                # therefore never return colliding stuff!
            else:
                return self._array[location].insert(el)
    
    
    def retrieve(self, key):
        # key needs to have some special properties:
        #   - it needs to be convertible to an int, of course returning the same
        #     int as converting the whole element to an int (which is then hashed)
        #
        #   - it also needs to have a unique value. this (probably non-int)
        #     value is used for chaining/probing.
        #     If we don't require this to be unique, chaining would be useless, as 
        #     the integer representations of all elements that need to be in some 
        #     kind of chain would all have the same (integer) searchkey (that's why 
        #     they are chained)!
        #     Probing would also be problematic, because it won't know when it found
        #     the right element.
        # Therefore, we require all elements to have a method .__dict__[self._attribute]
        # which returns a UNIQUE searchkey of a type so that it:
        #   - is convertible to an int (with int(el.__dict__[self._attribute]) )
        #   - has the operator '==' defined on it.
        # 
        # The argument 'key' for this function should be the UNIQUE key that would
        # have been returned by 'element.__dict__[self._attribute]', where element is the element
        # we look for.
        # 
        # A special case is when we store integers.
        # element.__dict__[self._attribute] will be the same as int(element.__dict__[self._attribute]).
        # However, you *will* need to define a wrapper class for the 'int' type.
        
        location = self._locationOf(key)
        
        if self._chaining == None:
            if location == -1:
                return None
            else:
                return self._array[location]
        else:
            if self._array[location] == None:
                return None
            else:
                # chaining class handles it from here
                return self._array[location].retrieve(key)
    
    
    def delete(self, key):
        location = self._locationOf(key)
        
        if self._chaining == None:
            if location == -1:
                return None
            else:
                self._array[location] = Deleted(key)
        else:
            if self._array[location] == None:
                return False
            else:
                # chaining class handles it from here
                return self._array[location].delete(key)
    
    
    def inorder(self):
        for el in self._array:
            if el != None:
                if self._chaining == None:
                    # simply yield the element
                    yield el
                else:
                    # yield all elements from chaining class
                    yield from el.inorder()
    
    
    def sort(self, attr, sortingFunc=sorting.bubblesort):
        templist = list(self.inorder())
        sortingFunc(templist, attr)
        for i in templist:
            yield i
    
    def isEmpty(self):
        for el in self.inorder():
            return False
        return True
    
    def __repr__(self):
        s = ""
        i = 0
        for el in self._array:
            s += "{}:\t{}\n".format(i, str(el))
            i+=1
        return s
        # return simple list of elements.
        

