class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        visitedPAC = set()
        visitedATL = set()
        visited = set()
        res = []

        def dfs(r,c,rOriginal,cOriginal):

            if (r,c) in visited:
                return 
      
            if r == 0 or c == 0:
                visitedPAC.add((rOriginal,cOriginal))
                
            
            if r == len(heights) - 1 or c == len(heights[0]) -1:
                visitedATL.add((rOriginal,cOriginal))
               
            
            visited.add((r,c))

            dirs = [(0,1),(0,-1),(1,0), (-1,0)]

            for dr, dc in dirs:
                if 0 <= (r + dr) < len(heights) and 0 <= (c + dc) < len(heights[0]) and heights[r][c] >= heights[r+dr][c+dc]:
                    dfs(r+dr,c+dc,rOriginal,cOriginal) 

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                dfs(i,j,i,j)
                if (i,j) in visitedPAC and (i,j) in visitedATL:
                    res.append([i,j])
                visited.clear()
        
        return res 


        
            
         
            
            
            


        