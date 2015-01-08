from hashmap import *

# read as 'int-able string'
class intableString:
    def __init__(self, s):
        self.s = s
        
    def __str__(self):
        return self.s
    
    def __repr__(self):
        return self.s
    
    def __int__(self):
        # for example, count all values of letters
        total = 0
        for l in self.s:
            total += ord(l)
        return total
   
    def __eq__(self, other):
        if self.s == other.s:
            return True
        return False

class fancyString:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def searchkey(self):
        return self.a
    def __str__(self):
        return str(self.a) + ":" + str(self.b)
    def __repr__(self):
        return self.__str__()

test_i = 1
successes = 0
failures = 0

def test(cond, oracle=True):
    global test_i
    global successes
    global failures
    if cond != oracle:
        print("!!! Error while executing test {}.".format(test_i))
        print("!!! Expected {}, but got {}".format(str(oracle), str(cond)))
        failures += 1
    else:
        print("passed test {}".format(test_i))
        successes += 1
    test_i += 1


python = fancyString(intableString("python"), "is interpreted")
onpyth = fancyString(intableString("onpyth"), "event-driven version of python")
haskell = fancyString(intableString("haskell"), "guaranteed to have no side effects, because no one will ever run it")
golang = fancyString(intableString("golang"), "go := (C++)--")
javascript = fancyString(intableString("js"), "please built a precompiler for me")
java = fancyString(intableString("java"), "will force OO-programming right in your face")
vaja = fancyString(intableString("vaja"), "like java, but vaja")
jvaa = fancyString(intableString("jvaa"), "like vaja, but jvaa")

ha = Hashmap(13, None, lineairProbing)

ha.hashMapInsert(python)
ha.hashMapInsert(onpyth)
ha.hashMapInsert(haskell)
ha.hashMapInsert(golang)
ha.hashMapInsert(javascript)
ha.hashMapInsert(java)
ha.hashMapInsert(vaja)
ha.hashMapInsert(jvaa)

print(ha)

print("==== basic tests ====")
test(ha.hashMapRetrieve(intableString("java")).b == "will force OO-programming right in your face")
test(ha.hashMapDelete(intableString("java")) != None)
test(ha.hashMapRetrieve(intableString("java")) == None)
test(ha.hashMapRetrieve(intableString("jvaa")).b == "like vaja, but jvaa")
test(ha.isEmpty(), False)
for el in ha.hashMapInorderTraversal():
    test(ha.hashMapDelete(el.searchkey()))
test(ha.isEmpty(), True)

print("==== chaining tests ====")
ha = Hashmap(23, None, None, Linkedchain)

ha.hashMapInsert(python)
ha.hashMapInsert(onpyth)
ha.hashMapInsert(haskell)
ha.hashMapInsert(golang)
ha.hashMapInsert(javascript)
ha.hashMapInsert(java)
ha.hashMapInsert(vaja)
ha.hashMapInsert(jvaa)

test(ha.hashMapRetrieve(intableString("java")).b == "will force OO-programming right in your face")
test(ha.hashMapDelete(intableString("java")) != None)
test(ha.hashMapRetrieve(intableString("java")) == None)
test(ha.hashMapRetrieve(intableString("jvaa")).b == "like vaja, but jvaa")
test(ha.isEmpty(), False)

print(ha)

for el in ha.hashMapInorderTraversal():
    test(ha.hashMapDelete(el.searchkey()))
test(ha.isEmpty(), True)

print(ha)

print("{} successes, {} failures".format(successes, failures))