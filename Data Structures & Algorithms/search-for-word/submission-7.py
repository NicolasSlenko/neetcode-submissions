class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False 

        globalWord = word

        def backtrack(i,j,word,curr):
            #ensure in bounds
            if word == "":
                return True
            if not (0 <= i < len(board) and 0 <= j < len(board[0])):
                return False
            
            #desired condition 
            if curr == globalWord:
                return True 
            
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if  0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == word[0]:
                    temp = board[i][j]
                    board[i][j] = "#"
                    if backtrack(nr,nc,word[1:],curr + word[0]):
                        return True
                    board[i][j] = temp

            return False 
 
        dirs = [(-1,0), (1,0), (0, -1), (0,1)] 
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == globalWord[0]:
                    if backtrack(i,j,word[1:],word[0]):
                        return True 
       
        return False 
        



            

            





        