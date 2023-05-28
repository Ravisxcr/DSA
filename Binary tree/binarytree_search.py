from root_data import *

# Searching in sorted Binary Tree
level = 0
def binary_tree_search(head,data):
    global level
    if head is None:
        return False
    if head.data == data:
        print("Data found at depth {}".format(level))
    elif head.data > data:
        level += 1
        binary_tree_search(head.left,data)
    else:
        level += 1
        binary_tree_search(head.right,data)

if __name__ == "__main__":
    binary_tree_search(root_2,1)
