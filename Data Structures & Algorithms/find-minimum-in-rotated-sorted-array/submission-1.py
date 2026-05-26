class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        ans = float('inf')
        while l <= r:
            m = (l+r)//2

            if nums[m] <= nums[r]:
                r = m - 1
                ans = min(ans, nums[m])
            else:
                l = m + 1
        return ans
                
            
