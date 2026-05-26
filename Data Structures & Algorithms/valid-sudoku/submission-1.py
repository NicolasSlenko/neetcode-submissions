class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row,board):
            seen = []
            rowd = board[row]
            for i in range(0, len(rowd)):
                if rowd[i] not in seen and rowd[i] != '.':
                    seen.append(rowd[i])
                elif rowd[i] == '.':
                    continue
                else:
                    return False
            return True 
        
        def checkColumn(numcol, board):
            seen = [] 
            column = [row[numcol] for row in board]
            for i in range(0, len(column)):
                if column[i] not in seen and column[i] != '.':
                    seen.append(column[i])
                elif column[i] == '.':
                    continue
                else:
                    return False
            return True 

        def checkSquares(board):
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    seen = set()
                    for i in range(3):
                        for j in range(3):
                            cell = board[box_row + i][box_col + j]
                            if cell != '.':
                                if cell in seen:
                                    return False
                                seen.add(cell)
            return True 




        for i in range(len(board[0])):
            if (checkRow(i, board) and checkColumn(i, board)):
                continue
            else:
                return False 

        if(checkSquares(board)):
            return True
        else:
            return False 

      
        