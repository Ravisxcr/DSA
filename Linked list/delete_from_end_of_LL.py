# Remove Nth Node From End of List

def removeNthFromEnd(head, n: int) :

    if head is None:
        return
    
    point = head
    curr = head
    for i in range(n):
        curr = curr.next

    if curr is None:
        return head.next

    while curr.next is not None:
        curr = curr.next
        point = point.next

    point.next = point.next.next
    return head

# Optimized Solution

def removeNthFromEnd(head, n: int) :
    curr = head 
    count = 1
    while(curr.next != None):
        curr = curr.next
        count += 1
    c = (count - n)
    new_curr = head
    i = 1
    while(i < c):
        new_curr = new_curr.next
        i += 1
    if(c == 0):
        return new_curr.next
    elif(new_curr.next != None):
        new_curr.next = new_curr.next.next 
        return head
    else:
        new_curr