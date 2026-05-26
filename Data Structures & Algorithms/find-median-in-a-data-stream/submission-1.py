class MedianFinder:

    def __init__(self):
        #max heap    #min heap
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        #add to small by default
        heapq.heappush(self.small, -1 * num)

        #make sure every element in small is <= element in large
        if (self.small and self.large) and (self.small[0] * -1 > self.large[0]):
            #move from small to large
            val = heapq.heappop(self.small) * -1 
            heapq.heappush(self.large, val)
        
        #make sure sizes are even

        #small is bigger than large, move from small to large
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) * -1 
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)
        

    def findMedian(self) -> float:
        #odd # of elements
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]

        #even number of elements
        return (self.small[0] * -1 + self.large[0]) /2

        
        