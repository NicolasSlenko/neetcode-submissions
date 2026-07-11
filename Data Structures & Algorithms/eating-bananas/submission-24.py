class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        h_taken = 0
        l = 1
        r = max(piles)
        k_best = max(piles)
     
        while l <= r:
            k = (l + r)//2
            print("k: " + str(k))
            for num in piles:
                if num <= k:
                    h_taken += 1
                elif num % k == 0:
                    h_taken += num//k
                else:
                    h_taken += (num//k + 1)
            print("h: " + str(h_taken))
            if h_taken <= h:
                k_best = k 
                r = k - 1
            else:
                l = k + 1
                if k > k_best:
                    return k_best
            h_taken = 0

        return k_best


        