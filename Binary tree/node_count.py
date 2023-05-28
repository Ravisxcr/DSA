from root_data import *

def numNodes(root):
    if root is None:
        return 0
    
    left = numNodes(root.left)
    right = numNodes(root.right)

    return 1 + left + right


if __name__ == '__main__':
    print(numNodes(root_1))