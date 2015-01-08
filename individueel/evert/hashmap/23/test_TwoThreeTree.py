# Author: Evert Heylen
# Test code for 2-3 tree.


from TwoThreeTree import *

t = TwoThreeTree()

t.isEmpty()
print("should be empty\n")

for i in range(8,1,-1):
    print("inserting",i)
    t.TwoThreeTreeInsert(i)

print("")

t.isEmpty()
print("should not be empty\n")

t.TwoThreeTreeInorderTraversal()
print("should be 2,3,4,5,6,7,8\n")

t.TwoThreeTreeRetrieve(5)
print("should be found\n")

t.TwoThreeTreeDelete(5)
print("should be deleted\n")

t.TwoThreeTreeRetrieve(5)
print("should not be found\n")

t.TwoThreeTreeInorderTraversal()
print("should be 2,3,4,6,7,8\n")