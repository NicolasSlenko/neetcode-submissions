class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = None 

        
    
        for i in range(len(nums)):
            val = nums[i]
            lookingFor = target - val 

            for j in range(i + 1, len(nums)):
                current = nums[j]
                if current == lookingFor:
                    return [i,j]


        
                

        