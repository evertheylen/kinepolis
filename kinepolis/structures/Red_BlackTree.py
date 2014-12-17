import Red_BlackNode

class Red_BlackTree:
    '''The class Red_BlackTree is the exact representation of the contract. All the methods are available for use in another program exept for create, this is not available in python and I used the standard initializer to do this. The implementation that is done in this class is fairly simple as most of the complicated calculation happen inside the Red_BlackNode module.'''
    def __init__(self, rootItem = None):
        '''Initialization of the Red_BlackTree class'''
        self.rootItem = Red_BlackNode.Node(rootItem)
        
    def destroyRed_BlackTree(self):
        '''Sets the root of the RedBlackTree to None therefore destroying it completely.'''
        self.rootItem = Red_BlackNode.Node(None)
        return True
    
    def isEmpty(self):
        '''Method to check if the tree is empty or not.'''
        if self.rootItem.item == None:
            return True
        else:
            return False
        
    def insert(self, newItem):
        '''The entire insert operation is implemented within the Red_BlackNode. It returns the result of this operation.'''
        return self.rootItem.insert(newItem, self) 
        
        
    def inorderTraversal(self, visit = None):
        '''Inorder Traversal is also implemented in the Red_BlackNode.'''
        print("De Inorder Traversal van de roodzwartboom, output is:")
        print("huidige knoop, linkerpointer, linkerknoop, rechterpointer, rechterknoop, ouder")
        return self.rootItem.inorderTraversal(visit)
    
    def retrieve(self, searchKey): 
        '''Retrieve returns de value that is found and doesn't change the tree.'''
        (success, value) = self.rootItem.retrieve(searchKey)
        print('De operatie was {0}, {1} is de gevonden waarde'.format(success, value))
        
    def delete(self, searchKey):
        '''The entire delete operation is implemented within the Red_BlackNode. It returns the result of this operation.'''
        return self.rootItem.delete(searchKey, self)
        
        
# Own testcode...        
'''boom = Red_BlackTree()
print(boom.isEmpty())
boom.insert(10)
print(boom.isEmpty())
boom.insert(100)
boom.insert(30)
boom.insert(80)
boom.insert(50)
boom.delete(10)
boom.insert(60)
boom.insert(70)
boom.insert(40)
boom.delete(80)
boom.insert(90)
boom.insert(20)
boom.delete(30)
boom.delete(70)
print(boom.rootItem)
boom.inorderTraversal()
print(boom.isEmpty())'''
