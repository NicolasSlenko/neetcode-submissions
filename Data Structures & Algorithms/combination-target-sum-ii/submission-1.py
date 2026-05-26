class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []

      
        def backtrack(i, curSum):
            if curSum == target:
                res.append(cur[:])
                return 
        
            if curSum > target or i >= len(candidates):
                return
         

            #include current value 
            cur.append(candidates[i])
            backtrack(i+1, candidates[i] + curSum)
            cur.pop()

            #don't include current value
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, curSum)
            
        
        backtrack(0,0)

      

        return res