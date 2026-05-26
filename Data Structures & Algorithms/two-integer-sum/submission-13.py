from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(list)

        for i in range(len(nums)):
            seen[nums[i]].append(i)

            if target - nums[i] in seen:
                first = min(i, seen[target - nums[i]][0])
                second = max(i, seen[target - nums[i]][0])
        
        return [first, second]