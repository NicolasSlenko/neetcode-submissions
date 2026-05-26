class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Helper to run DFS and count visited nodes
        def dfs(node, visited, graph):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited, graph)

        n = len(edges)
        for i in range(n - 1, -1, -1):
            # Build graph without edge i
            graph = {j: [] for j in range(1, n + 1)}
            for j, (u, v) in enumerate(edges):
                if i == j:
                    continue  # Skip current edge
                graph[u].append(v)
                graph[v].append(u)
            visited = set()
            dfs(1, visited, graph)
            if len(visited) == n:
                return edges[i] 
        