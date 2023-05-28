from root_data import *

prev = None

def bToDLL(root):
    if root is None:
        return root
    
    head = bToDLL(root.left)

    global prev

    if prev is None:
        head = root
    else:
        root.left = prev 
        prev.right = root

    prev = root

    bToDLL(root.right)
    return head



def printDLL(head):

    while head is not None:
        print(head.data," ")
        head = head.right

if __name__ == '__main__': 
    printDLL(bToDLL(root_1))