class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        best = 0

        for i in range(len(nums)):
            if nums[i] + 1 in numSet:
                continue 
            
            curr = 1
            while nums[i] - curr in numSet:
                curr +=1 
            
            if curr > best:
                best = curr
        

        return best
