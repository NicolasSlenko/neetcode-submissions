class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def bt(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                bt(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                bt(openN, closedN + 1)
                stack.pop()
        

        bt(0,0)
        return res


        