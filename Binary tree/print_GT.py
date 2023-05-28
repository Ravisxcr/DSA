from generic_tree_data import *
import queue

# Printing the Generic tree
def print_GT(root):
    if root is None:
        return
    
    print(root.data)
    for child in root.children:
        print_GT(child)

# Printing the Details of generic tree
def print_GT_detail(root):
    if root is None:
        return
    
    print("{} : ".format(root.data), end="")
    for child in root.children:
        print("{} ,".format(child.data), end = '')

    print()
    for child in root.children:
        print_GT_detail(child)
    
# Taking generic tree input recusively
def input_GT():
    print("Enter root Data")
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = TreeNode_arr(rootData)

    print("Enter number of children for ",rootData)
    childrenCount = int(input())
    for _ in range(childrenCount):
        child = input_GT()
        root.children.append(child)

    return root

# Counting the number of nodes in the generic tree
def numNode(root):
    if root is None:
        return 0
    
    count = 1
    for child in root.children:
        count = count + numNode(child)
    return count

# Taking levelwise input
def levelinput():
    q = queue.Queue()
    print("Enter the data :")
    data = int(input())
    if data == -1:
        return None
    
    root = TreeNode_arr(data)
    q.put(root)
    while (not(q.empty())):
        current_root = q.get()
        print("Enter the number of childre of : ",current_root.data)
        child_count = int(input())
        for i in range(child_count):
            print("Enter the child of : ",current_root.data)
            child_data = int(input())
            child_node = TreeNode_arr(child_data)
            root.children.append(child_node)
            q.put(child_node)
    return root



if __name__ == "__main__":
    # n1 = input_GT()
    # print_GT_detail(n1)
    # n1 = levelinput()
    print_GT_detail(n1)
