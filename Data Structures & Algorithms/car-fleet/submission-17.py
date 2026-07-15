class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        res = []

        for pos, speed in zip(position,speed):
            res.append([pos,speed])
        
        res.sort() 

        for pos, speed in res:
            
            time_car = (target-pos)/speed

            while stack and stack[-1] <= time_car:
                faster_time = stack.pop()

            stack.append((target - pos)/speed)
        
        return len(stack)


            

                    
    

        





        