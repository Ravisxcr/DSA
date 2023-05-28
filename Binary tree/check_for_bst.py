from root_data import *
from sortedarray_to_BST import *

def checkBST(root):
    if root is None:
        return True
    if root.left is not None and root.right is not None:
        return  root.data > root.left.data and root.right.data > root.data and checkBST(root.left) and checkBST(root.right)
    elif root.left is None and root.right is not None:
        return  (root.right.data > root.data) and checkBST(root.right)
    elif root.left is not None and root.right is None:
        return  (root.data > root.left.data)  and checkBST(root.left) 
    

# Improved solution

def is_BST(root):
    min_val = -100000
    max_val = 100000
    return BST_node(root,min_val,max_val)

def BST_node(root,min,max):
    if root is None:
        return True
    if root.data > max or root.data < min:
        return False
    else:
        return BST_node(root.left,min,root.data-1) and BST_node(root.right,root.data+1,max)

    

if __name__ == "__main__":

    b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


    val = checkBST(tree_maker(b))
    if val is None:
        print('Tree is BST')
    else:
        print('Tree is not BST')

    print(is_BST(tree_maker(b)))
    print(is_BST(root_2))