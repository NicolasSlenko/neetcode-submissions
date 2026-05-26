class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        if not edges:
            return True 

        adjList = {}

        for a, b in edges:
            if a not in adjList:
                adjList[a] = [b]
            else:
                adjList[a].append(b)
            
            if b not in adjList:
                adjList[b] = [a]
            else:
                adjList[b].append(a)

        visited = set()

        def dfs(i,prev):
            if i in visited:
                return False 
            
            visited.add(i)

            for child in adjList[i]:
                if child != prev:
                    if not dfs(child, i):
                        return False

            return True 


        return dfs(0,0) and len(visited) == n 
            



        
        



        
            

            

