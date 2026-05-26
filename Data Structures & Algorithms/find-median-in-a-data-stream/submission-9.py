class MedianFinder:

    def __init__(self):
        #max heap    #min heap
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

       
        #make sure small <= large
        if (self.small and self.large) and self.small[0] * -1 > self.large[0]:
            smaller = heapq.heappop(self.small) * -1
            bigger = heapq.heappop(self.large)
            heapq.heappush(self.small, bigger * -1)
            heapq.heappush(self.large, smaller)
        
        #if sizes differ too much, move from small to large
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large) 
            heapq.heappush(self.small, val * -1)

    

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (self.small[0] * -1 + self.large[0])/2
      
        
        