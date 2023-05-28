from head_data import *

# To check ith position of the linked list
def ll_ipos(head, index):
    if head == None:
        return
    
    else: 
        curr1 = head
        count = 0
        while(curr1.next != None and index > count):
            curr1 = curr1.next
            count+=1
        
        if count == index:
            print(curr1.data)
        elif curr1.next != None:
            print(curr1.data)
        else:
            print("Not present")

# To insert the element at the ith position
def ll_ipos_insert(head, index, data):
    if head == None:
        return
    
    else: 
        curr1 = head
        if curr1.next != None:
            curr2 = head.next
        count = 1
        while(curr2.next != None and index > count):
            curr2 = curr2.next
            curr1 = curr1.next
            count+=1
        
        new_node = Node(data)
        curr1.next= new_node
        new_node.next = curr2


if __name__ == '__main__':
    ll_ipos(h1,5)