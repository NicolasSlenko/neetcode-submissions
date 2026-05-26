class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curMin, curMax = 1,1

        for n in nums:
            temp = n * curMax
            curMax = max(n*curMax, n, n*curMin)
            curMin = min(temp, n, n*curMin)

            res = max(res, curMax)
        
        return res
        