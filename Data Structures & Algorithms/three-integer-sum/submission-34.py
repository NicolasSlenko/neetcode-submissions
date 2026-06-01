class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = defaultdict(int)
        res = []

        for num in nums:
            seen[num] += 1
        
        for i in range(len(nums)):
            seen[nums[i]] -= 1

            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                seen[nums[j]] -= 1
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
               
                target = -(nums[i] + nums[j])

                if seen[target] >= 1:
                    res.append([nums[i], nums[j], target])

            for j in range(i+1, len(nums)):
                seen[nums[j]] += 1
            

        return res
            






                
            



            
            

 
        