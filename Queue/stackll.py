class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class stackLL:
    
    def __init__(self) -> None:
        self.__head = None
        self.__count = 0

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.__head
        head = newNode
        self.__count += 1

    def isEmpty(self):
        return self.__count == 0
    
    def pop(self):
        if self.isEmpty() is True:
            print("Empty")
            return
        ele = self.__head.data
        self.__head = self.__head.next
        self.__count += 1
        return ele
    
    def size(self):
        return self.__count