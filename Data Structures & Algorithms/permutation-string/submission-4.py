class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        curMap = {}

        for char in s1:
            curMap[char] = curMap.get(char,0) + 1
        
        l = r = 0

        while r < len(s2):
            if r - l + 1 > len(s1):
                if s2[l] in curMap:
                    curMap[s2[l]] += 1
                l+=1
            if s2[r] in curMap:
                curMap[s2[r]] -= 1

            if max(curMap.values()) == 0:
                return True
            r+=1

        

        return False 


