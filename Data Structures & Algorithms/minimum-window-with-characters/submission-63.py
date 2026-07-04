class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or len(t) == 0 or len(s) == 0:
            return ""

        res = ""
        max_length = float('inf')

        if s == t:
            return s
        
        window = defaultdict(int)
        need = defaultdict(int)
        have_c = 0
        need_c = 0

        for char in t:
            need[char] += 1
        
        for key in need:
            need_c +=1 
        
        l = r = 0
        
        while r < len(s):
            window[s[r]] += 1
            if window[s[r]] == need[s[r]]:
                have_c += 1
            
            while have_c >= need_c:
                if r - l + 1 < max_length:
                    res = s[l:r+1]
                    max_length = r-l+1
                window[s[l]] = window.get(s[l], 0) - 1
                if window[s[l]] < need[s[l]]:
                    have_c -= 1
                l += 1
            r += 1

            
        return res
        

        