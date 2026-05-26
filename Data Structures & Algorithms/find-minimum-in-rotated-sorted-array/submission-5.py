class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = float('inf')
        while(l<=r):
            m = (l+r)//2

            if(nums[m] < minimum):
                minimum = nums[m]

            if(nums[r] < nums[m]):
                l = m + 1
            else:
                r = m - 1
        return minimum
        