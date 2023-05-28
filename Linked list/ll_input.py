from node import Node
from head_data import *

def ll_in():
    head = None
    tail = None
    
    m = input().split(' ')
    a = [int(ele) for ele in m]

    for i in a:
        new_node = Node(i)
        if head == None:
            head = new_node

        else:
            curr = head
            while(curr.next != None):
                curr = curr.next

            curr.next = new_node

    return head

def ll_pr(head):
    if head == None:
        return
    
    else: 
        curr = head
        while(curr.next != None):
            print(curr.data)
            curr = curr.next
        print(curr.data)

if __name__ == '__main__':
    ll_pr(h1)