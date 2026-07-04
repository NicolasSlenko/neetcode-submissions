class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val not in '+-*/':
                stack.append(int(val))
            else:
                if val == '+':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    new_val = val1 + val2
                    stack.append(new_val)
                elif val == '-':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    new_val = val2 - val1
                    stack.append(new_val)
                
                elif val == '*':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    new_val = val1 * val2
                    stack.append(new_val)

                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    new_val = int(val2 / val1)
                    stack.append(new_val)
            print(stack)

        
        return int(stack[0])

        