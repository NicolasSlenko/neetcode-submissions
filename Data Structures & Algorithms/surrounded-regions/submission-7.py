class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS = len(board)
        COLS = len(board[0])
        dirs = [(0,-1), (0,1), (1,0), (-1,0)]

        def dfs(i,j):
            if i < 0 or j < 0 or i == ROWS or j == COLS or board[i][j] != 'O':
                return 
        
            board[i][j] = 'T'
            for dr, dc in dirs:
                dfs(i+dr,j+dc)
        #Capture unsurrounded regions (O->T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS-1] or c in[0, COLS -1]):
                    dfs(r,c)

        #Capture surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
    
        #Put Ts back to Os 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
        