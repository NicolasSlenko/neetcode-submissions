class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        memo = {}
     
        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i >= n:
                return i == n
            
            memo[i] = dfs(i+1) + dfs(i+2)
            return memo[i]
        
        return dfs(0)

        