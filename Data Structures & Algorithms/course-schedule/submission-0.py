class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for src, dest in prerequisites:
            graph[src].append(dest)
        cycle = set()
        visit = set()

        def dfs(src):
            if src in cycle:
                return False
            if src in visit:
                return True
            
            cycle.add(src)
            for neighbor in graph[src]:
                if not dfs(neighbor):
                    return False
            cycle.remove(src)
            visit.add(src)
            
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        