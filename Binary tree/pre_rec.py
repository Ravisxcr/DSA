from root_data import *

# prerder traversal recursively
def printTreePre(root):
    if root is None:
        return
    print("node data is ", root.data)

    if root.left is not None:
        print("Left data ", root.left.data)
    if root.right is not None:
        print("right data ", root.right.data)

    printTreePre(root.left)
    printTreePre(root.right)

if __name__ == '__main__':
    printTreePre(root_1)