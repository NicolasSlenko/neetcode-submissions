class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        visitedPAC = set()
        visitedATL = set()
        
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r,c,visit,prevHeight):
            if (r,c) in visit or r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prevHeight:
                return 
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(COLS):
            dfs(0,c,visitedPAC, heights[0][c])
            dfs(ROWS - 1,c, visitedATL, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r,0, visitedPAC, heights[r][0])
            dfs(r, COLS - 1, visitedATL, heights[r][COLS-1])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visitedATL and (r,c) in visitedPAC:
                    res.append([r,c])
        
        return res



        
            
         
            
            
            


        