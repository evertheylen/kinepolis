import datetime

from datastruct import *
from klassen import *


res = Reservatie(5, 4, datetime.datetime.now(), 45, 78)
print(res)
print(type(res))

tickets = createDataStructure(structures.BinTree, "val")
cin = Cinema("Kine", 5, None, None, None, None, tickets)
print(cin)
print(type(cin))
print(type(cin.tickets))