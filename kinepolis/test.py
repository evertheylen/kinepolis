import datetime

from datastruct import *
from classes import *
from etc import *


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


def testDataStruct(name):
    print("\n\n---------- starting test for datastruct:",name)
    ds = createDataStructure(name, "ID")
    
    test("ds empty", ds.isEmpty(), True)
    
        #def __init__(self, ID, firstname, lastname, mail):
        #""" All string, except ID: int. """
        
        #self.ID = ID
        #self.firstname = firstname
        #self.lastname = lastname
        #self.mail = mail
    
    # just an array to test stuff, not the actual datastructure!
    users = [
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
        User(309, "jjjjj", "JJJJJ", "jjjjjmail"),
        User(310, "kkkkk", "KKKKK", "kkkkkmail"),
        User(311, "lllll", "LLLLL", "lllllmail"),
        User(312, "mmmmm", "MMMMM", "mmmmmmail"),
        User(313, "nnnnn", "NNNNN", "nnnnnmail"),
        User(314, "ooooo", "OOOOO", "ooooomail"),
        User(315, "ppppp", "PPPPP", "pppppmail"),
        User(316, "qqqqq", "QQQQQ", "qqqqqmail"),
        User(317, "rrrrr", "RRRRR", "rrrrrmail"),
        User(318, "sssss", "SSSSS", "sssssmail"),
        User(319, "ttttt", "TTTTT", "tttttmail"),
        User(320, "uuuuu", "UUUUU", "uuuuumail"),
        User(321, "vvvvv", "VVVVV", "vvvvvmail"),
        User(322, "wwwww", "WWWWW", "wwwwwmail"),
        User(323, "xxxxx", "XXXXX", "xxxxxmail"),
        User(324, "yyyyy", "YYYYY", "yyyyymail"),
        User(325, "zzzzz", "ZZZZZ", "zzzzzmail"),
    ]
    
    
    for u in users:
        ds.insert(u)
    
    test("ds empty2", ds.isEmpty(), False)
    
    inorderList = [u for u in ds.inorder()]
    
    test("ds inorder", inorderList[5].firstname, "ccccc")
    
    ds.delete(104)  # Delete Evert
    
    inorderList = list(ds.inorder())
    
    test("ds inorder after delete", inorderList[5].firstname, "ddddd")
    
    test("ds retrieve", ds.retrieve(307), users[10])
    test("ds retrieve2", ds.retrieve(104), None)
    
    ds.delete(307)
    test("ds retrieve after delete", ds.retrieve(307), None)
    
    # Also new :)
    sortedOnName = list(ds.sort("ID"))
    #print(sortedOnName)
    test("ds sort()", sortedOnName[0].firstname, "Anthony")
    for i in sortedOnName:
        print(i.firstname)
    
    # Must be done apart from eachother, or python will lose its mind (generators etc...)
    for u in [u for u in ds.inorder()]:
        ds.delete(u.ID)
    
    test("ds empty3", ds.isEmpty(), True)
    
    # Yes, this test is new :)
    test("ds attribute", ds.attribute(), "ID")
    
    
    print("-------------\n\n")



# Test here
testDataStruct("UnsortedArray")

