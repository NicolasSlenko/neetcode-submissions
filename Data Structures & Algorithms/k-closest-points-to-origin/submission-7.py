class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []
        heap  = []

        for x,y in points:
            heapq.heappush(heap, (-(x**2 + y**2), [x,y]))
            while len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            popped = heapq.heappop(heap)
            res.append(popped[1])
        
        
        
        
        return res
        