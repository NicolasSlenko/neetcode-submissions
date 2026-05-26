class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        cur = []
        
        if not digits:
            return []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(cur))
                return 
            choices = ""
            if digits[i] == '2':
                choices = "abc"
            
            elif digits[i] == '3':
                choices = "def"
            
            elif digits[i] == '4':
                choices = "ghi"
            
            elif digits[i] == '5':
                choices = "jkl"
            
            elif digits[i] == '6':
                choices = "mno"

            elif digits[i] == '7':
                choices = "pqrs"

            elif digits[i] == '8':
                choices = "tuv"

            else:
                choices = "wxyz" 

            for char in choices:
                cur.append(char)
                dfs(i+1)
                cur.pop()
            
        dfs(0)
        return res 

        