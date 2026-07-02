class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = r = 0
        maxLength = 0
        curLength = 0

        curMap = {}
        while r < len(s):
            curMap[s[r]] = curMap.get(s[r],0) + 1
            curLength += 1
            maxFreq = max(curMap.values())
            while maxFreq > 1 and l < r:
                curMap[s[l]] -= 1
                maxFreq = max(curMap.values())
                l += 1
                curLength -= 1

            maxLength = max(curLength, maxLength) 
            r+=1

        return maxLength 



        