class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        maxIsland = [0]

        def dfs(i,j):
            if not (0 <= i < len(grid)) or not(0<=j < len(grid[0])) or (i,j) in visited:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            visited.add((i,j))
        
            return 1 + dfs(i+1, j)+  dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = dfs(i,j)
                    maxIsland[0] = max(maxIsland[0], area)
        
        return maxIsland[0]
        

        
        