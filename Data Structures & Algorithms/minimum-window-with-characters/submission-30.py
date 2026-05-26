class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        have = {}

        for i in range(len(t)):
            need[t[i]] = need.get(t[i],0) + 1
            have[t[i]] = 0
        
        l = 0
        h = 0
        n = len(need)
        res = ""
        resLength = float('inf')

        for r in range(len(s)):
            
            if s[r] in have:
                have[s[r]] += 1
                if have[s[r]] == need[s[r]]:
                    h+=1 

            while h == n:
                length = r - l + 1
                if length < resLength:
                    resLength = length
                    res = s[l:r+1]
                if s[l] in have:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        h -= 1
                l += 1
        return res 
            
            




    


            


        


        

        
        