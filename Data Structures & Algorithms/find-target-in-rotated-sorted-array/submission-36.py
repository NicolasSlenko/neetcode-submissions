class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            #left part sorted
            if nums[m] >= nums[l]:
                if target > nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            #right part sorted 
            else:
                if target < nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1


        return -1 
        