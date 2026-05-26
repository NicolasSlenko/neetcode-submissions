class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return "" 
        
        need = Counter(t)
        have = Counter()

        r = l = 0 
        n = len(need.keys())
        h = 0
        maxLength = float('inf')
        res = ""

        while r < len(s):
            
            have[s[r]] += 1
            if s[r] in need and have[s[r]] == need[s[r]]:
                h += 1

            while h == n:
                currLength = r - l + 1
                if currLength < maxLength:
                    maxLength = currLength
                    res = s[l:r+1]
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    h -= 1
                l+=1
            r+=1
        return res




        


            
            




    


            


        


        

        
        