class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setWork = set(nums)
        if len(nums) == 0:
            return 0 
        gs = 1
        for num in nums:
            cs = 1
            while num - 1 in setWork:
                cs += 1
                num -= 1
            gs = max(gs,cs)
        
        return gs


            
        