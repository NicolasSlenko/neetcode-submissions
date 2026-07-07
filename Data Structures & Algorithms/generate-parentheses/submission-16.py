class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []


        def bt(numOpened, numClosed):
            if numOpened == numClosed == n:
                res.append("".join(stack))
                return 
            
            if numOpened < n:
                stack.append("(")
                bt(numOpened + 1, numClosed)
                stack.pop()
            
            if numClosed < numOpened:
                stack.append(")")
                bt(numOpened, numClosed + 1)
                stack.pop()
        
        bt(0,0)
        return res

        
    



        