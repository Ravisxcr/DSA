from root_data import *

# post order traversal recursively
def printTreePost(root):
    if root is None:
        return

    if root.left is not None:
        print("Left data ", root.left.data)
    print("node data is ", root.data)
    if root.right is not None:
        print("right data ", root.right.data)

    printTreePost(root.left)
    printTreePost(root.right)

if __name__ == '__main__':
    printTreePost(root_1)
    print()
    printTreePost(root_m1)
    print()
    printTreePost(root_m2)