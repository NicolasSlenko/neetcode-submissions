class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i: [] for i in range(numCourses)}   # ensure every course exists
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visited = set()
        visiting = set()

        def dfs(course: int) -> bool:
            # cycle found
            if course in visiting:
                return False
            # already verified this subgraph has no cycle
            if course in visited:
                return True

            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)      # mark as done/acyclic
            return True

        # Check every course (graph may be disconnected)
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True 


        
        