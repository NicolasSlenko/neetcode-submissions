class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        arr = []
        time = []
        for pos, speed in zip(position, speed):
            arr.append([pos, speed])
        
        arr = sorted(arr, reverse = True)

        for pos, speed in arr:
            t = (target-pos)/speed
            time.append(t)

            if len(time) >= 2 and time[-1] <= time[-2]:
                time.pop()
        
        return len(time)
            

            

                    
    

        





        