from node import BinaryNode
from print_relation import *

def tree_maker(arr):
    length = len(arr)
    if length == 0:
        return None
    mid = length//2
    root = BinaryNode(arr[mid])
    root.left = tree_maker(arr[:mid])
    if mid != length:
        root.right = tree_maker(arr[mid+1:])
    return root

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9]
    printTree2(tree_maker(a))
