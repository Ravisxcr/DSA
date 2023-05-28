from root_data import *

def printTree2(root):
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
    printTree2(root.left)
    printTree2(root.right)

if __name__ == '__main__':
    printTree2(root_1)
    print()
    printTree2(root_m1)
    print()
    printTree2(root_m2)