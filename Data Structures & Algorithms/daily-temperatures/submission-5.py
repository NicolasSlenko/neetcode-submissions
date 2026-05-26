class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        stack = []
        for i in range(n):
            while(stack and temperatures[i] > stack[-1][0]):
                day = stack.pop()
                distance = i - day[1]
                output[day[1]] = distance
            stack.append((temperatures[i],i))
        
        return output 


        