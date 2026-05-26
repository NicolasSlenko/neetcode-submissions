class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False 
    
        col = []

        for i in range(len(matrix)):
            col.append(matrix[i][0])
        
        l = 0 
        r = len(col) - 1
        
        while l <= r:
            m = (l + r) // 2
          
            if col[m] <= target <= matrix[m][-1]:
                return self.binarySearch(matrix[m], target) != -1
            
            if col[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False 

    def binarySearch(self, nums, target):  
            l , r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid 
                
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return -1 
