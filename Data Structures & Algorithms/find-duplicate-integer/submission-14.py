class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for index, val in enumerate(nums):
            curr = abs(val)
            if nums[curr - 1] < 0:
                return curr
            else:
                nums[curr - 1] *= -1
            

        