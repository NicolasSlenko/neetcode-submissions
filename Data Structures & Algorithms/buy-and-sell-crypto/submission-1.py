class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) == 1):
            return 0 
        
        l = 0
        r = 1
        maxProfit = 0

        while(r < len(prices)):
            #profitable
            if(prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                if(profit > maxProfit):
                    maxProfit = profit
            #not profitable 
            else:
                l = r
            r+=1

            
            

        

        return maxProfit if maxProfit > 0 else 0