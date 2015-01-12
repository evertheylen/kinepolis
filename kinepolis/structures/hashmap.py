# Author: Evert Heylen
# Testcode door: Stijn Janssens


# By default, we can use the (unsorted) linked chain
from structures.uslinkedchain import USLinkedChain

import sorting

def lineairProbing(x):
    return x

def quadraticProbing(x):
    return x**2


def createModFuncString(mod):
    # Problem:  pickle doesn't save lambda's.
    # Solution: don't use lambda's, instead use strings and python's eval() function!
    return "lambda x: x%"+str(mod)



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
    pass


class Hashmap:
    def __init__(self, attr, length=23, hashFuncString=None, collisionSolution = USLinkedChain, toInt = int):
        # attr is a string, length is an int, hashFuncString is a string, collisionSolution is either a class or a function, toInt is a function
        
        # For example, if you want to create a hashmap with quadraticProbing,
        # length 51 and the default mod function, you write:
        #    hm = Hashmap("ID", 51, None, quadraticProbing)
        
        # If you want to create a hashmap with Linkedchain chaining, you write:
        #    hm = Hashmap("ID", 23, None, Linkedchain)
        
        self._attribute = attr
        self._array = [None]*length
        self._length = length
        
        if type(collisionSolution) == type:  # meaning: it's a class
            self._chaining = collisionSolution  # chaining class
            self._addressFunc = None
        else:  # it's not a class
            self._chaining = None
            self._addressFunc = collisionSolution
            # function to calculate next address, be it by probing or double hashing
        
        # Default hashFuncString
        # Why use strings?
        # because pickle can't pickle lambda's, but it can pickle strings.
        # therefore, the string is the function, and it gets eval'd everytime you want
        # to use the hashFunc.
        if hashFuncString == None:
            hashFuncString = createModFuncString(self._length)
        
        # The hashing function string.
        self._hashFuncString = hashFuncString
        
        # the toInt function will be called to convert the searchkey, defined by attr (using __dict__[attr]),
        # to an integer. By default, this is the builtin int() function, but this can be altered.
        
        # the toInt function should be consistent across restarts
        # i.e. don't use hash()!
        self._toInt = toInt
    
    def _hashFunc(self):
        return eval(self._hashFuncString)  # eval!
        # to call the hashing function you'd then have to do self._hashFunc()( argument )
    
    def attribute(self):
        return self._attribute
    
    def _key(self, element):
        return element.__dict__[self.attribute()]
    
    def _locationOf(self, key, inserting=False):
        """ Private function to calculate the location in the array of some element.
        Note that the element does not need to be in the array. """
        
        # 'inserting' will be the difference between doing a real search (retrieve, delete) (=False)
        # and searching for the best place to insert (=True)
        
        # if True, we'll keep an extra variable that contains the best place to insert.
        # we'll still return the correction location if the key is found, but if we don't find it, we
        # return the location of the best place to insert.
        
        location = self._hashFunc()(self._toInt(key))
        origloc = location
        
        if self._chaining == None:  # probing
            to_insert = -1  # see above
            
            #checked = [False] * self._length
            i = 1
            reached = False
            while i <= self._length:    # simple solution to prevent looping
                
                if inserting and (type(self._array[location]) == Deleted or self._array[location] == None) and to_insert == -1:
                    # we found a good place to insert!
                    to_insert = location
                    
                # stop looping when:
                #   - the current element is None
                #   X (the current element is of type Deleted and we're just looking for the best spot to insert)
                #   - the element is found
                if self._array[location] == None \
                    or (type(self._array[location]) != Deleted and self._key(self._array[location]) == key):
                    
                    reached = True
                    break
                
                location = origloc + self._addressFunc(i)
                
                # modulo location, so that it'll never reach an index not in our array
                location = location % self._length
                i+=1
            
            # If we have reached the right element...
            if reached:
                # if we're inserting, return to_ins if the object is NOT found
                if inserting:
                    if self._array[location] != None and type(self._array[location]) != Deleted:
                        # object found
                        return -1  # don't insert, it's already in here
                    else:
                        return to_insert
                else:
                    # not inserting, just return location
                    return location
            else:
                return to_insert  # no need to check for inserting, it should still have it's default value of -1
                # if we're inserting though, we should return it because it may hold a good place to insert. (otherwise -1)
                # else, it's still -1.
        
        else:  # chaining
            return location
    
    
    def insert(self, el):
        location = self._locationOf(self._key(el), True)  # we're just looking for the best spot to insert
            
        if self._chaining == None:  # we use probing
            if location == -1:
                return False
            
            # if the location isn't -1; we still need to check whether or not the desired location is already
            # occupied...
            if self._array[location] == None or (type(self._array[location]) == Deleted and True): #self._array[location].key == self._key(el)):
                # if it's either None or a deleted element
                self._array[location] = el
                return True
            # else...
            return False
        
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
        location = self._locationOf(key)
        
        if self._chaining == None:  # probing
            if location == -1:
                return None
            else:
                if type(self._array[location]) == Deleted:
                    return None
                # else...
                return self._array[location]
        else:  # chaining
            if self._array[location] == None:
                return None
            else:
                # chaining class handles it from here
                return self._array[location].retrieve(key)
    
    
    def delete(self, key):
        location = self._locationOf(key)
        
        if self._chaining == None:
            if location == -1:
                return False
            else:
                if type(self._array[location]) == Deleted or self._array[location] == None:
                    return False
                self._array[location] = Deleted()
                return True
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
        

