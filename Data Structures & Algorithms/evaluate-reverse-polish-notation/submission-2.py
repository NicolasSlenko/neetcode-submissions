class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if len(token) == 1:
                if token in '0123456789':
                    stack.append(int(token))
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()

                    if token == '+':
                        val = val1 + val2
                    elif token == '-':
                        val = val2 - val1
                    elif token == '/':
                        val = int(val2 / val1)
                    else:
                        val = val1 * val2 
                    stack.append(val)
            else:
                stack.append(int(token))
        
        return stack[-1]

        