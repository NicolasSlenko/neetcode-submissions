class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid[r][c] == '0':
                return 

            visited.add((r,c))
                
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        visited = set()
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '0':
                    if (i,j) not in visited:
                        dfs(i,j)
                        count += 1

        return count
                    
        

        
            