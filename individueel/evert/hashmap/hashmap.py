# Author: Evert Heylen

from Linkedchain import *

# een hashmap die instelbaar via een parameter kan switchen tussen een hashmap 
# met linear probing, quadratic probing en een hashmap met separate chaining 
# (zorg ervoor dat de gebruikte implementatie voor seperate chaining makkelijk 
# kan aangepast worden, begin bijvoorbeeld met de dubbel gelinkte ketting, maar 
# zorg dat die makkelijk kan aangepast worden naar een andere implementatie). 


def lineairProbing(x):
    return x

def quadraticProbing(x):
    return x**2


def createModFunc(mod):
    return lambda x: x % mod

class Hashmap:
    def __init__(self, length=23, hashFunc=None, addressFunc=lineairProbing, chaining=None):
        # chaining is a class, hashFunc and addressFunc are both functions.
        # If chaining is None, we don't chain.
        # If addressFunc is None, we will utilize the chaining method.
        # If they are both not None, we will utilize the chaining method
        
        self._array = [None]*length
        self._length = length
        
        if hashFunc == None:
            # default hashing function
            hashFunc = createModFunc(length)
        self._hashFunc = hashFunc
        
        self._addressFunc = addressFunc
        
        self._chaining = chaining
    
    def hashMapInsert(self, el):
        # el can be of every type, but it needs to be convertible to an int in some way.
        # see below.
        location = self._hashFunc(int(el.searchkey()))
        
        checked = [False] * self._length
        i = 0
        while self._array[location] != None and self._chaining == None:
            checked[location] = True
            if all(checked):
                return False    # All spots are taken!
            
            # This spot is already taken and we don't chain
            location += self._addressFunc(i)
            
            # Make location 'loop', so that it'll never reach an index not in our array
            location = location % self._length
            
            i+=1
            
        if self._chaining == None:
            # just insert!
            self._array[location] = el
        else:
            if self._array[location] == None:
                # Create a new instance of the desired chaining class
                self._array[location] = self._chaining()
                self._array[location].insert(el)
                # el should have a method .searchkey(), because reusing the int()
                # functionality will also be problematic for the chaining, as it
                # will have the same issues as the hashmap. .searchkey() should
                # therefore never return colliding stuff!
            else:
                self._array[location].insert(el)
    
    
    def hashMapRetrieve(self, key):
        # key needs to have some special properties:
        #   - it needs to be convertible to an int, of course returning the same
        #     int as converting the whole element to an int (which is then hashed)
        #
        #   - it also needs to have another unique value. this (probably non-int)
        #     value is used for chaining/probing.
        #     If we don't require this to be unique, chaining would be useless, as 
        #     the integer representations of all elements that need to be in some 
        #     kind of chain would all have the same int (that's why they are 
        #     chained)!
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
        # A special case is when we store integers, and we use the default mod function.
        # element.searchkey() will be the same as int(element.searchkey()).
        # However, you will need to define a wrapper class for the 'int' type.
        
        location = self._hashFunc(int(key))
        
        checked = [False] * self._length
       
        if self._chaining == None:
            checked = [False] * self._length
            i=0
            while self._array[location].searchkey() != key:
                checked[location] = True
                if all(checked):
                    return None    # All spots have been checked, it's not here!
                
                location += self._addressFunc(i)
                
                # Make location 'loop', so that it'll never reach an index not in our array
                location = location % self._length
                i+=1
            # By this point we've reached the right location
            return self._array[location]
        else:
            # The chaining class will take care of it from now.
            return self._array[location].retrieve(key)
    
    
    def hashMapDelete(self, key):
        location = self._hashFunc(int(key))
        
        checked = [False] * self._length
       
        if self._chaining == None:
            checked = [False] * length
            i = 0
            while self._array[location].searchkey() != key:
                checked[location] = True
                if all(checked):
                    return False    # All spots have been checked, it's not here!
                
                location += self._addressFunc(i)
                
                # Make location 'loop', so that it'll never reach an index not in our array
                location = location % self._length
                i+=1
            # By this point we've reached the right location
            self._array[location] = None # Delete
            return True
        else:
            # The chaining class will take care of it from now.
            el = self._array[location].remove(key)
            # We won't delete empty chains
            if el != None:
                return True # Succes!
            return False # Not so much succes.
    
    def __repr__(self):
        s = ""
        i = 0
        for el in self._array:
            s += "{}:\t{}\n".format(i, str(el))
            i+=1
        return s
        

