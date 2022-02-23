class MedianFinder:

    def __init__(self):
        self.max_heap, self.min_heap = [], []


    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -1* num)
        
        # Maintain lesser than equal to condition
        if self.max_heap and self.min_heap:
            if -1*self.max_heap[0] > self.min_heap[0]:
                val = -1* heappop(self.max_heap)
                heappush(self.min_heap, val)
        
        # Checks if size is uneven
        if len(self.max_heap)  > len(self.min_heap) + 1:
            val = -1* heappop(self.max_heap)
            heappush(self.min_heap, val)
            
        if len(self.min_heap)  > len(self.max_heap) + 1:
            val = heappop(self.min_heap)
            heappush(self.max_heap, -1*val)
            

    def findMedian(self) -> float:
        # Odd Length Condition
        if len(self.max_heap)  > len(self.min_heap):
            return -1*self.max_heap[0]
        elif len(self.min_heap)  > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (-1*self.max_heap[0]+self.min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()