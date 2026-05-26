class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set()
        total = 0

        for i in range(len(nums)):
            myset.add(nums[i])


        for i in nums:
            currentTotal = 0
            while(i+1 in myset):
                currentTotal += 1
                i+=1
            total = max(total,currentTotal)
        
        return total + 1 if nums else 0