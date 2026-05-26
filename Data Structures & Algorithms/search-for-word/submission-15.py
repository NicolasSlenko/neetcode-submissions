class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return False 

        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def dfs(row,col,i):
            if i >= len(word):
                return True 

            char = word[i]
            if not(0 <= row < ROWS) or not(0 <= col < COLS) or board[row][col] != char or (row,col) in visited:
                return False 
            
            
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]

            for dr, dc in dirs:
                visited.add((row,col))
                if dfs(row + dr, col + dc, i + 1):
                    return True 
                visited.remove((row, col))

            return False 
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True 
        
        return False 
        



            

            





        