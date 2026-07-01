class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        currMap = {}
        l = r = 0
        while r < len(s):
            currMap[s[r]] = currMap.get(s[r], 0) + 1
            max_freq = max(currMap.values()) if currMap else 0
            while not(r - l + 1 - max_freq <= k):
                currMap[s[l]] -= 1
                l += 1
        
           
            maxLength = max(maxLength, r - l + 1)
            r += 1
    
        return maxLength


                

