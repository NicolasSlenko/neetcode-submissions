class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}

        for val in nums:
            count[val] = count.get(val, 0) + 1


        for num, cnt in count.items():
            heapq.heappush(heap, (cnt, num))

            if len(heap) > k:
                heapq.heappop(heap) 
        res = []   

        for cnt, num in heap:
            res.append(num)

        return res    


