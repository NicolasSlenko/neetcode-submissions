class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

    
        for i in range(len(nums) - k + 1):
            curr = nums[i:i+k]
            output.append(max(curr))
        
        return output 
