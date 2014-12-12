# Author: Evert Heylen
# Testcode door: Stijn Janssens


# As an example, we can use the Linkedchain
from Linkedchain import *



def lineairProbing(x):
    return x

def quadraticProbing(x):
    return x**2


def createModFunc(mod):
    return lambda x: x % mod



################
# Some documentation:
#
# When inserting, the class of the objects inserted should implement the function .searchkey().
# The function .searchkey() should be of type A, so that type A:
#    - is convertible to an int (__int__ must be implemented)
#    - can be used with the '==' operator (__eq__ must be implemented)
#
# When searching for or deleting based on a searchkey, that searchkey should be UNIQUE, and it
# should be of type A mentioned above. If we're looking for object B with searchkey C, the
# following should be true:
#     B.searchkey() == C
# 
# If you want to chain, you should offer some class as the chaining class. That class should
# offer the following functions:
#    - insert(obj)
#      return whether it was succesful.
#
#    - retrieve(key)
#      return the full element. (key is of type A!)
#      if it's not found, return None.
#
#    - remove()
#      return the full element, and remove it.
#      if removing fails, return None.
#
#    - inorder()
#      a generator that yields all possible elements.
#
# On top of that, it should be capable of initializing without parameters.
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
class Hashmap:
    def __init__(self, length=23, hashFunc=None, addressFunc=lineairProbing, chaining=None):
        # chaining is a class, hashFunc and addressFunc are both functions.
        # If chaining is None, we don't chain.
        # If addressFunc is None, we will utilize the chaining method.
        # If they are both not None, we will utilize the chaining method
        
        # For example, if you want to create a hashmap with quadraticProbing,
        # length 51 and the default mod function, you write:
        #    hm = Hashmap(51, None, quadraticProbing)
        
        # If you want to create a hashmap with Linkedchain chaining, you write:
        #    hm = Hashmap(23, None, None, Linkedchain)
        
        self._array = [None]*length
        self._length = length
        if hashFunc == None:
            # default hashing function
            hashFunc = createModFunc(length)
            
        self._hashFunc = hashFunc
        self._addressFunc = addressFunc
        self._chaining = chaining
    
    def hashMapInsert(self, el):
        # el can be of every type, but it needs to offer the .searchkey() function,
        # which should be convertible to an int. (see above)
        location = self._hashFunc(int(el.searchkey()))
        origloc = location
        
        checked = [False] * self._length
        i = 1
        while self._array[location] != None and self._chaining == None:
            checked[location] = True
            #print("loc:",location, checked)
            if all(checked):
                return False    # All spots are taken!
            
            # This spot is already taken and we don't chain, so calculate next location
            # with the _addressFunc.
            location = origloc + self._addressFunc(i)
            # Make location 'loop', so that it'll never reach an index not in our array
            location = location % self._length
            
            i+=1
            
        if self._chaining == None:
            # just insert!
            self._array[location] = el
            return True
        else:
            if self._array[location] == None:
                # Create a new instance of the desired chaining class
                self._array[location] = self._chaining()
                return self._array[location].insert(el)
                # el should have a method .searchkey(), because reusing the int()
                # functionality will also be problematic for the chaining, as it
                # will have the same issues as the hashmap. .searchkey() should
                # therefore never return colliding stuff!
            else:
                return self._array[location].insert(el)
    
    
    def hashMapRetrieve(self, key):
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
        # Therefore, we require all elements to have a method .searchkey()
        # which returns a UNIQUE searchkey of a type so that it:
        #   - is convertible to an int (with int(el.searchkey()) )
        #   - has the operator '==' defined on it.
        # 
        # The argument 'key' for this function should be the UNIQUE key that would
        # have been returned by 'element.searchkey()', where element is the element
        # we look for.
        # 
        # A special case is when we store integers.
        # element.searchkey() will be the same as int(element.searchkey()).
        # However, you *will* need to define a wrapper class for the 'int' type.
        
        location = self._hashFunc(int(key))
        #print("location =", location)
        origloc = location
        
        if self._chaining == None:
            checked = [False] * self._length
            i=1
            while not all(checked):
                checked[location] = True
                #print("location =", location)
                if self._array[location] != None and self._array[location].searchkey() == key:
                    break
                
                location = origloc + self._addressFunc(i)
                
                # Make location 'loop', so that it'll never reach an index not in our array
                location = location % self._length
                i+=1
            # By this point we've reached the right location
            if all(checked):
                return None
            return self._array[location]
        else:
            if self._array[location] != None:
                # The chaining class will take care of it from now.
                return self._array[location].retrieve(key)
            else:
                return None
    
    
    def hashMapDelete(self, key):
        location = self._hashFunc(int(key))
        origloc = location
        if self._chaining == None:
            checked = [False] * self._length
            i = 1
            while not all(checked):
                checked[location] = True
                if self._array[location] != None and self._array[location].searchkey() == key:
                    break
                
                location = origloc + self._addressFunc(i)
                
                # Make location 'loop', so that it'll never reach an index not in our array
                location = location % self._length
                i+=1
            # By this point we've reached the right location
            if self._array[location] != None:
                self._array[location] = None # Delete
                return True
            else:
                return False    # the right location did not contain the element
        else:
            if self._array[location] != None:
                # The chaining class will take care of it from now.
                el = self._array[location].remove(key)
                # We won't delete empty chains
                if el != None:
                    return True # Succes!
                return False # Not so much succes, not in the chain object
            else:
                return False # Not in this array
    
    
    def hashMapInorderTraversal(self):
        for el in self._array:
            if el != None:
                if self._chaining == None:
                    # simply yield the element
                    yield el
                else:
                    for el_subelement in el.inorder():
                        yield el_subelement
    
    
    def isEmpty(self):
        for el in self.hashMapInorderTraversal():
            return False
        return True
    
    
    def destroyHashMap(self):
        del(self)
    
    def __repr__(self):
        s = ""
        i = 0
        for el in self._array:
            s += "{}:\t{}\n".format(i, str(el))
            i+=1
        return s
        # return simple list of elements.
        

