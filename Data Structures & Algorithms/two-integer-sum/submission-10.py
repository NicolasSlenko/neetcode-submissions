class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visited = {}

        for i in range(len(nums)):
            if target - nums[i] in visited:
                other = visited[target - nums[i]]
                smaller = min(i,other)
                bigger = max(i, other)

                return [smaller,bigger]
            
            visited[nums[i]] = i


        
        