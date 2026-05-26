class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, curr, totalSum):
            if totalSum == target:
                res.append(curr[:])
                return
            
            if index >= len(candidates) or totalSum > target:
                return 
            
            #include value
            curr.append(candidates[index])
            dfs(index, curr, totalSum + candidates[index])
        
            #don't include value
            curr.pop()
            dfs(index + 1, curr, totalSum)
        
        dfs(0,[],0)

        return res




      
            
