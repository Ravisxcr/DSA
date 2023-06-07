# My sol
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        return None

    def pop(self) -> None:
        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
    
#optimized sol

class MinStack:

    def __init__(self):
        self.ds = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            if val <= self.mins[-1]:
                self.mins.append(val)
        self.ds.append(val)

    def pop(self) -> None:
        if self.ds[-1] == self.mins[-1]:
            self.mins.pop()
        self.ds.pop()

    def top(self) -> int:
        return self.ds[-1] 

    def getMin(self) -> int:
        return self.mins[-1]
        