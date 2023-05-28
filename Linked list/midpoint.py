def ll_mid(head):
    if head == None:
        return
    
    else: 
        curr1 = head
        curr2 = head
        count = 0
        while(curr1.next != None and curr2.next.next != None):
            curr1 = curr1.next
            curr2= curr2.next.next
            count+=1
        
        print(count)


if __name__ == '__main__':
    print('HI')