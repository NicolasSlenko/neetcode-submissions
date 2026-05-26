class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        cur = []

        def backtrack(i):
            if i >= len(nums):
                output.append(cur[:])
                return 
            
            cur.append(nums[i])
            backtrack(i+1)
        
            cur.pop()
            backtrack(i+1)
    


        backtrack(0)
        return output 