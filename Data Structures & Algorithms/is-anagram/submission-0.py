class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        slist = [] 
        tlist = []

        if(len(s) != len(t)):
            return False 

        for i in range(len(s)):
            slist.append(s[i])
            tlist.append(t[i])
        
        slist.sort()
        tlist.sort()

        for i in range(len(slist)):
            if slist[i] != tlist[i]:
                return False 


        return True

        