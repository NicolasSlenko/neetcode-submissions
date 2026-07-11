class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False 
        t = l = 0
        b = len(matrix) - 1
        r = len(matrix[0]) - 1

        while t <= b:
            m = (b + t)//2
            if target >= matrix[m][l] and target <= matrix[m][r]:
                while l <= r:
                    mid = (l + r)//2
                    if target == matrix[m][mid]:
                        return True 
                    
                    if target > matrix[m][mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False
            elif target > matrix[m][r]:
                t = m + 1
            elif target < matrix[m][l]:
                b = m - 1
        
        return False 



        