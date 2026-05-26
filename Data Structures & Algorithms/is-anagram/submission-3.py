from collections import defaultdict 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        
        seenS = defaultdict(int)
        seenT = defaultdict(int)

        for i in range(len(s)):
            seenS[s[i]] += 1
            seenT[t[i]] += 1

        if seenS != seenT:
            return False 

        return True

        