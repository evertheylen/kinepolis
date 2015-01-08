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
    try:
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
        
        
        for u in users:
            ds.push(u)
        
        test("ds empty2", ds.isEmpty(), False)
        

        test("ds getTop1", ds.getTop(), users[28])

        test("ds pop", ds.pop(), users[27])
        
        test("ds getTop2", ds.getTop(), users[27])
        
        ds.destroyStack()
        
        test("ds empty3", ds.isEmpty(), True)
        
        # Yes, this test is new :)
        test("ds attribute", ds.attribute(), "ID")
        
        
        print("-------------\n\n")
    except Exception as e:
        print(rgbtext(str(e)))


# Test here

testDataStruct("Stack")

