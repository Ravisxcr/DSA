from root_data import *
from height import height

def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    return lh == rh

if __name__ == '__main__':
    print(isBalanced(root_1), " ",isBalanced(root_m1))