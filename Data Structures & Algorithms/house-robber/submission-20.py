class Solution:
    def rob(self, nums: List[int]) -> int:
                  
        n = len(nums)
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]
  
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i>= n:
                return 0
            
            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]
        
        return dfs(0)
            



        
