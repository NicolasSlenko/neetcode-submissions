class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones) * -1
            stone2 = heapq.heappop(stones) * -1

            if stone1 == stone2:
                continue
            else:
                bigger = max(stone1,stone2)
                smaller = min(stone1,stone2)

                newWeight = bigger - smaller
                heapq.heappush(stones, newWeight * -1) 
        
        if len(stones) == 0:
            return 0
        else:
            return stones[0] * -1
            
