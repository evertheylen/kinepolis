
class Node:
    def __init__(self, data):
        self.data = data
        self.prv = None
        self.nxt = None
    
    def __repr__(self):
        return repr(self.data)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def length(self):
        return self.length
    
    def enqueue(self, item):
        if self.length == 0:
            self.head = Node(item)
            self.tail = self.head
        else:
            newnode = Node(item)
            #print('newnode is',newnode)
            newnode.prv = self.tail
            #print('newnode.prv is',self.tail)
            newnode.prv.nxt = newnode
            #print('newnode.prv.nxt =',newnode)
            self.tail = newnode
            #print('self.tail =',newnode)
        self.length += 1
        return True # success
    
    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            head = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return head.data
        else:
            head = self.head
            self.head.nxt.prv = None
            self.head = head.nxt
            self.length -= 1
            return head.data
    
    def getFront(self):
        if self.length == 0:
            return None
        return self.head.data
    
    def inorder(self):
        nextptr = self.head
        while nextptr != None:
            yield nextptr.data
            nextptr = nextptr.nxt
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        s = '['
        for el in self.inorder():
            s += ' '+str(el)
        return s + ' ]'
 



# Tests
'''def main():
    qu = Queue()
    qu.enqueue(5)
    qu.enqueue(6)
    qu.enqueue('test')
    print(qu)
    print(qu.getFront())
    print(qu.dequeue())
    print(qu.getFront())
    print(qu.dequeue())
    print(qu.getFront())

    print(qu)
    print(qu.dequeue())

    try:
        qu.dequeue()
    except Exception as e:
        print(e)

    print(qu)

    try:
        qu.getFront()
    except Exception as e:
        print(e)

    qu.destroyStack()

    """
    # 'stresstest'
    qu = Queue()

    import random
    for i in range(500000):
        qu.enqueue(random.randint(1,500))
        qu.enqueue(random.randint(1,500))
        qu.dequeue()
    """


if __name__=='__main__':
    main()'''
