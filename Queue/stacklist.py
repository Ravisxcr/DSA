class StackList:

    def __init__(self) -> None:
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) == 0:
            print("Stack is empty")
            return
        return  self.__data.pop()
    
    def size(self):
        return (len(self.__data))
    
    def isEmpty(self):
        return self.size() == 0
    
    def top(self):
        if len(self.__data) == 0:
            print("Stack is empty")
            pass
        ele = self.__data[-1]
        return ele
