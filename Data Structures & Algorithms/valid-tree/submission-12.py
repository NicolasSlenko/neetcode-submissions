class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        preMap = {i: [] for i in range(n)}

        for c1, c2 in edges:
            preMap[c1].append(c2)
            preMap[c2].append(c1)
        
        visited = set()

        def dfs(node, prev):
            
            if node in visited:
                return False 
            
            visited.add(node)

            for child in preMap[node]:
                if child == prev:
                    continue 
                
                if not dfs(child, node):
                    return False 
            
            return True 
        
        return dfs(0, "") and len(visited) == n 
        



        
            

            

