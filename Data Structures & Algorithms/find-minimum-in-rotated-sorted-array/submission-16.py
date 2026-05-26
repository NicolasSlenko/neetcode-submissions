class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0 
        r = len(nums) - 1
        minVal = float('inf')

        while l <= r:
            m = (l+r)//2
            minVal = min(minVal, nums[m])
            if nums[m] > nums[l] and nums[m] < nums[r]:
                r = m - 1
            elif nums[m] < nums[l] and nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        

        return minVal 




        
                
            
