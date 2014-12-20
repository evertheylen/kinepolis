# Could be used as an example for other datatstructures

import sorting

class USArray:
    def __init__(self, attribute):
        self.array = []
        self._attribute = attribute

    def attribute(self):
        return self._attribute

    def insert(self, el):
        if self.attribute() not in el.__dict__.keys():
            # print("Wrong type!")
            return False

        self.array.append(el)
        return True

    def retrieve(self, key):
        # simple sequential search
        for el in self.array:
            if el.__dict__[self.attribute()] == key:
                return el
        return None

    def delete(self, key):
        el = self.retrieve(key)
        if el is None:
            return False
        self.array.remove(el)
        return True

    def isEmpty(self):
        if len(self.array) == 0:
            return True
        return False

    def sort(self, attr, sortFunc = sorting.bubblesort):
        # because this is an UnsortedArray, we change the order of the array itself
        self.array = sortFunc(self.array, attr)
 
        # 'passthrough' of another generator
        yield from self.inorder()

    def inorder(self):
        """ For an UnsortedArray, it's not sure to be sorted.
        It's basically whatever order it is in"""

        for el in self.array:
            yield el
