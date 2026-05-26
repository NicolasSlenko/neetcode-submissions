class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ', '') 
        s = "".join(c for c in s if c.isalpha() or c.isnumeric())

        print(s)

        x = 0
        y = len(s) - 1 

        while(x <= y):
            if s[x] != s[y]:
                return False
            x += 1
            y -= 1
        

        return True 
    
    
        