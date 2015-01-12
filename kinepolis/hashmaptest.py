from datastruct import *
from classes import *
from sorting import *

import random

usersarr = {
    322: User(322, "Emma", "Stone", "pieterstalktmij@celebmail.com"),
    101: User(101, "Pieter", "Coeck", "ikstalkemma@sldfj.com"),
    102: User(102, "Stijn", "Janssens", "sdflkdlkdfj_stijn"),
    103: User(103, "Anthony", "Hermans", "mailanthony"),
    104: User(104, "Evert", "Heylen", "mailevert"),
    302: User(302, "ccccc", "CCCCC", "cccccmail"),   # 5
    303: User(303, "ddddd", "DDDDD", "dddddmail"),
    304: User(304, "eeeee", "EEEEE", "eeeeemail"),
    316: User(316, "qqqqq", "QQQQQ", "qqqqqmail"),
    322: User(322, "wwwww", "WWWWW", "wwwwwmail"),
    311: User(311, "lllll", "LLLLL", "lllllmail"),
    312: User(312, "mmmmm", "MMMMM", "mmmmmmail"),
    318: User(318, "sssss", "SSSSS", "sssssmail"),
    319: User(319, "ttttt", "TTTTT", "tttttmail"),
    320: User(320, "uuuuu", "UUUUU", "uuuuumail"),
    343: User(343, "rrrrr", "RRRRR", "rrrrrmail"),
    366: User(366, "AAAvvvvv", "VVVVV", "vvvvvmail"),
}


keys = list(usersarr.keys())
keys_in_hm = [311, 322]


ha = structures.Hashmap("ID", 23, None, structures.hashmap.quadraticProbing)

#for u in usersarr.values():
    #ha.insert(u)

ha.insert(usersarr[322])
ha.insert(usersarr[311])

errors = 0

for _ in range(50000):
    if bool(random.randint(0,1)):
        # inserting
        oldha = str(ha)
        key_to_insert = keys[random.randint(0,len(keys)-1)]
        
        expected = True
        if key_to_insert in keys_in_hm:
            expected = False
        else:
            keys_in_hm.append(key_to_insert)
        
        if expected != ha.insert(usersarr[key_to_insert]):
            print("\n!!!!!!!!!!! Insert went wrong. expected",expected)
            print(keys_in_hm)
            print('----------------------')
            print(oldha)
            print('----------------------')
            print(ha)
            errors+=1
        print("ha.insert(usersarr[%d])"%key_to_insert)
        
        
    elif len(keys_in_hm) > 2:
        oldha = str(ha)
        
        key_to_delete = keys_in_hm[random.randint(0,len(keys_in_hm)-1)]
        
        expected = True
        if key_to_delete not in keys_in_hm:
            expected = False
        else:
            keys_in_hm.remove(key_to_delete)
        
        if expected != ha.delete(key_to_delete):
            print("\n !!!!!!!!!! delete went wrong. expected", expected)
            print(keys_in_hm)
            print('----------------------')
            print(oldha)
            print('----------------------')
            print(ha)
            errors+=1
        print("ha.delete(%d)"%key_to_delete)
    else:
        print("pass")
            

print(errors)

raise Exception()
