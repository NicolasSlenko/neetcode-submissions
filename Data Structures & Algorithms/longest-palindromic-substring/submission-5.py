class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s
        

        def isPalindrome(substr):
            l = 0
            r = len(substr) - 1
            length = len(substr) 
            if length % 2 == 0:
                while l < r:
                    if substr[l] != substr[r]:
                        return False 
                    l+=1
                    r-=1
                return True 
            else:
                while l != r:
                    if substr[l] != substr[r]:
                        return False 
                    l+=1
                    r-=1
                return True 
        
        maxLength = float('-inf')
        maxSub = ""

        for i in range(len(s)):
            for j in range(len(s) + 1):
                curr = s[i:j]
                if isPalindrome(curr) and len(curr) > maxLength:
                    maxLength = len(curr)
                    maxSub = curr
        
        return maxSub
                
