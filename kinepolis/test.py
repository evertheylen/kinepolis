import datetime

from datastruct import *
from classes import *
import sorting

from etc import *

from random import shuffle

import traceback
import copy

def testClasses():
    res = Reservatie(5, 4, datetime.datetime.now(), 45, 78)
    print(res)
    print(type(res))

    tickets = createDataStructure(structures.BinTree, "val")
    cin = Cinema("Kine", 5, None, None, None, None, tickets)
    print(cin)
    print(type(cin))
    print(type(cin.tickets))


def test(name, t, oracle=True):
    if t != oracle:
        print(rgbtext("test {} went wrong!\nExpected {}, but got {}.".format(name, oracle, t)))
    else:
        print("test {}: succes! got: {}".format(name, t))


# just an array to test stuff, not the actual datastructure!
usersarr = [
    User(100, "Emma", "Stone", "pieterstalktmij@celebmail.com"),
    User(101, "Pieter", "Coeck", "ikstalkemma@sldfj.com"),
    User(102, "Stijn", "Janssens", "sdflkdlkdfj_stijn"),
    User(103, "Anthony", "Hermans", "mailanthony"),
    User(104, "Evert", "Heylen", "mailevert"),
    User(302, "ccccc", "CCCCC", "cccccmail"),   # 5
    User(303, "ddddd", "DDDDD", "dddddmail"),
    User(304, "eeeee", "EEEEE", "eeeeemail"),
    User(305, "fffff", "FFFFF", "fffffmail"),
    User(306, "ggggg", "GGGGG", "gggggmail"),
    User(307, "hhhhh", "HHHHH", "hhhhhmail"),   # 10
    User(308, "iiiii", "IIIII", "iiiiimail"),
    User(323, "xxxxx", "XXXXX", "xxxxxmail"),
    User(324, "yyyyy", "YYYYY", "yyyyymail"),
    User(325, "zzzzz", "ZZZZZ", "zzzzzmail"),
    User(309, "jjjjj", "JJJJJ", "jjjjjmail"),
    User(310, "kkkkk", "KKKKK", "kkkkkmail"),
    User(313, "nnnnn", "NNNNN", "nnnnnmail"),
    User(314, "ooooo", "OOOOO", "ooooomail"),
    User(315, "ppppp", "PPPPP", "pppppmail"),
    User(316, "qqqqq", "QQQQQ", "qqqqqmail"),
    User(322, "wwwww", "WWWWW", "wwwwwmail"),
    User(311, "lllll", "LLLLL", "lllllmail"),
    User(312, "mmmmm", "MMMMM", "mmmmmmail"),
    User(318, "sssss", "SSSSS", "sssssmail"),
    User(319, "ttttt", "TTTTT", "tttttmail"),
    User(320, "uuuuu", "UUUUU", "uuuuumail"),
    User(317, "rrrrr", "RRRRR", "rrrrrmail"),
    User(321, "AAAvvvvv", "VVVVV", "vvvvvmail"),
]


def testDataStruct(name, **kwargs):
    try:
        print("\n\n---------- starting test for datastruct:",name)
        ds = createDataStructure(name, "ID", **kwargs)
        
        test("ds empty", ds.isEmpty(), True)
        
            #def __init__(self, ID, firstname, lastname, mail):
            #""" All string, except ID: int. """
            
            #self.ID = ID
            #self.firstname = firstname
            #self.lastname = lastname
            #self.mail = mail
        
        users = copy.deepcopy(usersarr)
        
        for u in users:
            ds.insert(u)
        
        test("ds empty2", ds.isEmpty(), False)
        
        inorderList = list(ds.inorder())
        
        test("ds inorder", inorderList[5].firstname, "ccccc")

        ds.delete(104)  # Delete Evert

        inorderList = list(ds.inorder())
        
        test("ds inorder after delete", inorderList[5].firstname, "ddddd")
        
        test("ds retrieve", ds.retrieve(307), users[10])
        test("ds retrieve2", ds.retrieve(104), None)
        
        ds.delete(307)
        test("ds retrieve after delete", ds.retrieve(307), None)
        
        # Also new :)
        sortedOnName = list(ds.sort("firstname"))
        test("ds sort()", sortedOnName[0].firstname, "AAAvvvvv")
        
        sortedOnLastName = list(ds.sort("lastname", sorting.quicksort))
        test("ds sort()", sortedOnLastName[-1].lastname, "ZZZZZ")
        
        # Must be done apart from eachother, or python will lose its mind (generators etc...)
        for u in list(ds.inorder()):
            ds.delete(u.ID)
        
        test("ds empty3", ds.isEmpty(), True)
        
        # Yes, this test is new :)
        test("ds attribute", ds.attribute(), "ID")
        
        
        print("-------------\n\n")
        
    except Exception as e:
        print(rgb(255,0,0))
        traceback.print_exc()
        print(endc)


def testSortingAlgo(algo):
    users = copy.deepcopy(usersarr)
    shuffle(users)  # shuffle users
    algo(users, "firstname")     # sort them again
    test("sort "+algo.__name__, users[-1].firstname, "zzzzz")
    test("sort_empty "+algo.__name__, algo([], "ID"), [])


# Tests here
if __name__=='__main__':
    # ------- Data structures
    testDataStruct("SLinkedChain")
    testDataStruct("USLinkedChain")
    testDataStruct("USArray")
    testDataStruct("Hashmap")
    # inorder tests will fail, this is normal and should not be considered an error
    # also, watch out with using a non-chaining method, the hashmap may get filled up
    
    testDataStruct("BinTree")
    #testDataStruct("TwoThreeTree")
    
    # ------- Sorting methods
    totest = []
    for algoname in list(sorting.__dict__.keys()):
        # small hack to only test sorting algorithms
        if algoname[-4:] == "sort":
            totest.append(algoname)
    print(totest)
    
    #for algoname in ['heapsort']:
    for algoname in sorted(totest):
        print("\ntesting",algoname)
        testSortingAlgo(sorting.__dict__[algoname])
    
    
