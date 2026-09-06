class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            self.left.append(-num)
            return

        if self.left and -self.left[0] <= num:
            heapq.heappush(self.right, num)
        elif self.right and self.right[0] > num:
            heapq.heappush(self.left, -num)
        elif self.right and self.right[0] < num:
            heapq.heappush(self.right, num)
        elif self.left and -self.left[0] >= num:
            heapq.heappush(self.left, -num)
        
        diff = len(self.left) - len(self.right)
        if diff > 1:
            heapq.heappush(self.right, -(heapq.heappop(self.left)))
        elif diff < -1:
            heapq.heappush(self.left, -(heapq.heappop(self.right)))



    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        if len(self.left) > len(self.right):
            return -self.left[0]
        return self.right[0]
        