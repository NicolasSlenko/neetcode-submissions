class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        total = 0

        for num in myset:
            if num - 1 not in myset:
                current = num
                streak = 1
            
                while current + 1 in myset:
                    streak+=1
                    current+=1
            
                total = max(total, streak)

        return total