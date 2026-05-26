class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False 

        visited = set()

        def dfs(node, prev):
            
            if node in visited:
                return False 
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor != prev and not dfs(neighbor, node):
                    return False
            
            return True 

            
        graph = {i:[] for i in range(n)}

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        
        
        return dfs(0, "")
        
        


        
            

            

