"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        adjList = {}
        adjList[node] = Node(node.val)

        q = collections.deque()
        q.append(node)

        while q:
            cur = q.popleft()
            for child in cur.neighbors:
                if child not in adjList:
                    adjList[child] = Node(child.val)
                    q.append(child)
                adjList[cur].neighbors.append(adjList[child])
        
        return adjList[node]
        

        