class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = r = 0
        cMap = defaultdict(int)
        max_length = 0
        while l <= r and r < len(s):
            cMap[s[r]] += 1
            max_freq = max(cMap.values())
            if r - l + 1 - max_freq <= k:
                max_length = max(max_length, r-l+1)
            while r - l + 1 - max_freq > k:
                cLength = r - l
                print(cLength)
                max_length = max(max_length, cLength)
                max_freq = max(cMap.values())
                cMap[s[l]] -= 1
                l += 1
            r += 1

    
        


        return max_length


                

