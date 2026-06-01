class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        seen = defaultdict(int)
        

        for i, num in enumerate(nums):
            seen[num] += 1

        heap = []

        for num, freq in seen.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for pair in heap:
            res.append(pair[1])
        
        return res
        
    

        
        



