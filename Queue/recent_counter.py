class RecentCounter:

    def __init__(self):
        self.arr = []
        self.pin = 0

    def ping(self, t: int) -> int:
        self.arr.append(t)
        while len(self.arr)>0 and (t - self.arr[0]) >3000:
            self.arr.pop(0)
        return len(self.arr)
            