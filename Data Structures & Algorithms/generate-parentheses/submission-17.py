class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []


        def bt(numOpened, numClosed):
            if numOpened == numClosed == n:
                res.append("".join(stack))
        
            if numClosed < numOpened:
                stack.append(")")
                bt(numOpened, numClosed + 1)
                stack.pop()
        
            if numOpened < n:
                stack.append("(")
                bt(numOpened + 1, numClosed)
                stack.pop()
        bt(0,0)
        return res




        
        
    



        