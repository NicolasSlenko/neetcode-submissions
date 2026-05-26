class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
    
        def dfs(i, cur, total):
            #goal
            if total == target:
                res.append(cur[:])
                return 
            
            #stop looking, base case
            if i >= len(candidates) or total > target:
                return 

            #include this value
            cur.append(candidates[i])

            #no restriction, include candidate
            dfs(i,cur,total + candidates[i])

            #reset
            cur.pop()

            #don't include current candidate
            dfs(i+1,cur,total)
        dfs(0, [], 0)
        return res
            
