class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if stack:
                    end = stack.pop()
                    if char == ')' and end != '(':
                        return False 
                    if char == '}' and end != '{':
                        return False
                    if char == ']' and end != '[':
                        return False 
                else:
                    return False 
                    
        
        
        return True if not stack else False 

        