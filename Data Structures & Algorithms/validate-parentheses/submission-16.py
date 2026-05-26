from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        if len(s) % 2 == 1:
            return False 
        

        for i in range(len(s)):  
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if s[i] == '}':
                    if len(stack) == 0 or stack.pop() != '{':
                        return False
                if s[i] == ')':
                    if len(stack) == 0 or stack.pop() != '(':
                        return False
                if s[i] == ']':
                    if len(stack) == 0 or stack.pop() != '[':
                        return False
                
                 
        return True if len(stack) == 0 else False
        