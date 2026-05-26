class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(-1,0), (1,0), (0,1),(0,-1)]
        q = collections.deque()
        time = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                    
        
        while q:
            for _ in range(len(q)):
                pos = q.popleft()
                i = pos[0]
                j = pos[1]
                for dr, dc in dirs:
                    if 0 <= i + dr < ROWS and 0 <= j + dc < COLS and grid[i+dr][j+dc] == 1:
                        grid[i+dr][j+dc] = 2
                        q.append((i+dr,j+dc)) 
            if q:
                time += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return time
        
            
        