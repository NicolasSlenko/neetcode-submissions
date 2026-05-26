class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = collections.deque()
        gatesPos = []
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    gatesPos.append((i,j))
        

        for gate in gatesPos:
            q.append(gate)

        step = 1
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr, dc in dirs:
                        if 0 <= i + dr < ROWS and 0 <= j + dc < COLS and grid[i+dr][j+dc] == 2147483647:
                            grid[i+dr][j+dc] = step
                            q.append((i+dr,j+dc))
            step += 1




        