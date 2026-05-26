class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 

        cnt = Counter()
        maxLength = 0
        l = r = 0 

        while r < len(s):
            cnt[s[r]] += 1
            while (r - l + 1) - max(cnt.values()) > k:
                cnt[s[l]] -= 1
                l+=1 
            maxLength = max(r-l+1, maxLength)
            r+=1 
        
        return maxLength 



        
            

                

        


        