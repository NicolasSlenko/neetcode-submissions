class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        #scan individual string to check balanced
        def is_valid(s):
            balance = 0

            for c in s:
                if c == "(":
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False 
            
            return not balance 


        def dfs(s):
            if len(s) == 2 * n and is_valid(s):
                res.append(s)
                return
            
            if len(s) > 2 * n:
                return 

            dfs(s + ")")
            dfs(s + "(")
        
        dfs("")

        return res
    



        