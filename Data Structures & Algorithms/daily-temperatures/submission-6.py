class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if stack:
                while stack and stack[-1][0] < temperatures[i]:
                    day = stack.pop()
                    temp = day[0]
                    pos = day[1]
                    res[pos] = i - pos
            
            stack.append((temperatures[i], i))
        
        return res



