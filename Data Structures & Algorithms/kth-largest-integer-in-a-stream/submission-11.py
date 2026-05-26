import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        copy = self.nums.copy()
        heapq.heapify(copy)      
        while len(copy) > self.k:
            heapq.heappop(copy)
        
        return copy[0]
