class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        if(len(heights) == 2):
            return min(heights[0], heights[1])

        l = 0
        r = len(heights) - 1
        maxa = 0

        while (l < r):
            currentArea = min(heights[l],heights[r]) * (r - l)
            if(currentArea > maxa):
                maxa = currentArea 
            if(heights[l] < heights[r]):
                l+=1
            else:
                r-=1
        

        return maxa


        