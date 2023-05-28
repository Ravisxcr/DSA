from node import BinaryNode
import queue

def LevelInput():
    q = queue.Queue()
    print('Enter root')
    rootData = int(input())
    if rootData == -1:
        return None
    else:
        root  = BinaryNode(rootData)
        q.put(root)

    while not(q.empty()):
        current_node = q.get()
        
        print("Enter left child of ", current_node.data)
        l_data = int(input())
        if l_data != -1:
            leftchild = BinaryNode(l_data)
            current_node.left = leftchild
            q.put(leftchild)

        print("Enter right child of ", current_node.data)
        r_data = int(input())
        if r_data != -1:
            rightchild = BinaryNode(l_data)
            current_node.left = rightchild
            q.put(rightchild)

    return root