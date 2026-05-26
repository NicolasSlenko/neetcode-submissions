class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {0:0}

        def dfs(amount):
            if amount in memo:
                return memo[amount]

            res = 1e9

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res
        minCoins = dfs(amount)
        return minCoins if minCoins < 1e9 else -1
        
        