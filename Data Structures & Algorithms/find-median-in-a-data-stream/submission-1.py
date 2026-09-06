class MedianFinder:

    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        self.vals.append(num)
        self.vals.sort()

    def findMedian(self) -> float:
        n = len(self.vals)
        m = n // 2
        if n % 2 == 0:
            return (self.vals[m] + self.vals[m - 1]) / 2
        return self.vals[m]
        