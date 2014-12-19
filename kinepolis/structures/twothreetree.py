#Auteur: Anthony Hermans

class Node:
    def __init__(self, data = None, parent = None, children = None):
        self.data = data
        self.parent = parent
        self.children = children

    def __str__(self):
        return str(self.data)

class TwoThreeTree():

    def __init__(self, root=None, leftchild=None, midchild=None, rightchild=None, size=0 ):
        self.root = root
        self.leftchild = leftchild
        self.midchild = midchild
        self.rightchild = rightchild
        self.size = size

    def __str__(self):
        return str(self.root)

    def deleteTwoThreeTree(self):
        current = self.root
        for i in range(self.size):
            del current
            current = self.root.next
            i = i - 1
        message = "De 2-3 boom is verwijderd."
        #print(message)
        return

    def isEmpty(self):
        if self.size == 0:
            #print("De 2-3 boom is leeg.")
            return

        else:
            #print("De 2-3 boom is niet leeg.")
            return


    def insert(self, data):
        new = Node(data)
        if self.size <=3 :
            if self.size == 0:
                self.root = new
                self.size += 1
            else:
                if data < self.root.data :
                    if self.leftchild != None:
                        self.leftchild = new
                        self.size += 1
                    else:
                        self.leftchild = Node(data)
                        self.size += 1
                else:
                    if self.rightchild != None:
                        self.rightchild = new
                        self.size += 1
                    else:
                        self.rightchild = Node(data)
                        self.size += 1

    def delete(self, searchkey):
        if self.root.data == searchkey:
            self.root = self.rightchild
            self.size-=1
        else:
            if searchkey < self.root.data:
                if self.leftchild == searchkey:
                    self.leftchild = None
                    self.size-=1
                else:
                    #print("Zit niet in deze boom")
            if self.root.data < searchkey and searchkey < self.root.data:
                if self.midchild.data == searchkey:
                    self.midchild = None
                else:
                    #print("Item is niet gevonden")

            if searchkey >= self.root.data:
                if self.rightchild.data == searchkey:
                    self.rightchild = None
                    self.size-=1
                else:
                    #print("Zit niet in deze boom")

    def retrieve(self, searchkey):
        if self.root.data == searchkey:
            #print("Item "+ str(searchkey) + " is gevonden")
        else:
            if searchkey < self.root.data:
                if self.leftchild.data == searchkey:
                    #print("Item "+ str(searchkey) + " is gevonden")
                else:
                    #print("Item is niet gevonden")
            if self.root.data < searchkey and searchkey < self.root.data:
                if self.midchild.data == searchkey:
                    #print("Item "+ str(searchkey) + " is gevonden")
                else:
                    #print("Item is niet gevonden")
            if searchkey > self.root.data:
                if self.rightchild.data == searchkey:
                    #print("Item "+ str(searchkey) + " is gevonden")
                else:
                    #print("Item is niet gevonden")

    def inorder(self):
        i = 0
        current = self.root
        while current != None:
            if i == 1:
                current = self.root.data
                yield current
            if i == 0 and self.leftchild != None:
                current = self.leftchild.data
                yield current
            if i > 1 and self.rightchild != None:
                current = self.rightchild.data
                yield current
            i+=1
            if i == self.size:
                break
