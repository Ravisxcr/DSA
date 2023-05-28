from root_data import *

def checkTree(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return True
    
    sum = 0
    if root.left is not None:
        sum += root.left.data
    if root.right is not None:
        sum += root.right.data

    return (sum == root.data) and checkTree(root.left) and checkTree(root.right)

if __name__ == '__main__':
    print(checkTree(root_1), " ",checkTree(root_m1))