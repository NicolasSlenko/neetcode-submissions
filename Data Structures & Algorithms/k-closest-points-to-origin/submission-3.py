class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []
        pointmap = {}
        temp = []

        for x,y in points:
            pointmap[(x,y)] = math.sqrt(x**2 + y**2)
        
        
        for key, val in pointmap.items():
            temp.append((val,key))
        
        heapq.heapify(temp)

        for i in range(k):
            popped = heapq.heappop(temp)
            res.append(list(popped[1]))
        
        return res
        