class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        dirs = [(-1,0), (1,0), (0,-1),(0,1)]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    #print("test")
                    if 0 <= r + dr < ROWS and 0 <= c + dc < COLS and grid[r+dr][c+dc] == 2147483647:
                        print("test")
                        grid[r+dr][c+dc] = 1 + grid[r][c]
                        q.append((r+dr,c+dc))






        