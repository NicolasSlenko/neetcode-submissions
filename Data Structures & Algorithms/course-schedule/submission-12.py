class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i: [] for i in range(numCourses)}

        for crs1, crs2 in prerequisites:
            preMap[crs1].append(crs2)
        
        visited = set()

        def dfs(node):
            if preMap[node] == []:
                return True

            if node in visited:
                return False 
            
            visited.add(node)

            for connection in preMap[node]:
                if not dfs(connection):
                    return False 
            
            visited.remove(node)

            return True 
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True 






        
        