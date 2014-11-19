import Node
import Linkedchain
import Stack

'''Testcode voor de modules Node en Linkedlist.'''

n1 = Node.Node()
print(n1)
n1.item = 86
print(n1)
n2 = Node.Node('banaan')
print(n2)
n1.next = (n2)
print(n1)
print(n2)
n3 = Node.Node('hallo')
l = Linkedchain.Linkedchain()
print(l)
l.insert(n3)
print(l)
l.insert(n2,n3)
print(l)
l.insert(n1,n3,n2)
print(l)
l.remove(n3)
print(l)
l.head = n3
print(l)
l.remove(n1)
print(l)

'''Testcode voor de module Stack.'''

stack = Stack.Stack()
print(stack)
stacktop = Node.Node(42)
stack.destroyStack()
print(stack.isEmpty())
stack.push(stacktop)
print(stack)
stack.push(n2)
print(stack)
stack.push(n1)
print(stack)
stack.pop()
print(stack)
print(stack.pop())
print(stack)
print(stack.getTop())
print(stack)
stack.pop()
print(stack)

'''Testcode voor de dubbel gelinkte ketting.'''

dubbele = Linkedchain.DoublyLinkedchain()
dubbele.insert(n3)
print(dubbele)
print(n3.precede, n3.next)
dubbele.insert(n2,n3)
print(n2.precede, n2.next)
print(dubbele)
dubbele.insert(n1,n3,n2)
print(dubbele)
print(n1.precede, n1.next)
print(n2.precede, n2.next)
