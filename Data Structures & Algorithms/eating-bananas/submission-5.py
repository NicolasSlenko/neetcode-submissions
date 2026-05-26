class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 0
        r = max(piles)
        min_k = r 

        while l <= r:
            m = (l + r)//2 
            
            if(m != 0 and self.helper(piles,h,m)):
                min_k = m 
                r = m - 1
            else:
                l = m + 1

        return min_k 
    

    def helper(self, piles, h, k):
        h_took = 0

        for p in piles:
            h_need = math.ceil(p/k)
            h_took += h_need 
        
        return h_took <= h 


        