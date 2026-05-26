class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        seen = set()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and nums[i-1] == a:
                continue 
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                currSum = nums[i] + nums[l] + nums[r]

                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1 
                else:
                    if (nums[i],nums[l],nums[r]) not in seen:
                        res.append([nums[i],nums[l],nums[r]])
                        seen.add((nums[i],nums[l],nums[r]))
                    r -= 1
        return res 
            


        