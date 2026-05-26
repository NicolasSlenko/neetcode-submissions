class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        parent = {}
        cycle_nodes = set()
        cycle_found = False

        def dfs(node, prev):
            nonlocal cycle_found
            visited.add(node)
            parent[node] = prev

            for neighbor in graph[node]:
                if neighbor == prev:
                    continue 
                
                if neighbor not in visited:
                    dfs(neighbor, node)
                    if cycle_found:
                        return 
                else:
                    cycle_found = True
                    cycle_nodes.add(neighbor)
                    cur = node
                    while cur != neighbor:
                        cycle_nodes.add(cur)
                        cur = parent[cur]
                    return 
        dfs(1,-1)

        for u,v in reversed(edges):
            if u in cycle_nodes and v in cycle_nodes:
                return [u,v]
        return []
            
        