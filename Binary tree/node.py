class BinaryNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class TreeNode_arr:
    def __init__(self, data):
        self.data = data
        self.children = list()

class BST:
    def __init__(self) -> None:
        self.root = None
        self.numNode = 0

    def printHelper(self, root):
        # printing for root node
        if root is None:
            return
        else:
            print("\n node data is ", root.data , end=' ')

        # printing for left node
        if root.left is not None:
            print("Left data ", root.left.data, end=' ')
        else:
            print("Left data is None", end=' ')

        # printing for right node
        if root.right is not None:
            print("right data ", root.right.data, end='')
        else:
            print("right data is None ", end=' ')

        # Calling for left node and right node
        self.printHelper(root.left)
        self.printHelper(root.right)

    def printTree(self):
        return self.printHelper(self.root)
    
    def searchHelper(self, root, data):
        if root is None:
            return None
        if root.data == data:
            return True
        if root.data > data:
            return self.searchHelper(root.left, data)
        else:
            return self.searchHelper(root.right, data)
        
    def isPresent(self, data):
        return self.searchHelper(self.root, data)
    
    def insertHelper(self, root, data):
        if root is None:
            node = BinaryNode(data)
            return node
        
        if root.data > data:
            root.left = self.insertHelper(root.left, data)
        else:
            root.right = self.insertHelper(root.right, data)

    def insert(self, data):
        self.numNode +=1
        self.root = self.insertHelper(self.root, data)

    


