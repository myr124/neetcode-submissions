class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(lambda:[])
        res = []

        for src, dst in prerequisites:
            adjList[src].append(dst)

        cycle = set()
        seen = set()



        def dfs(src):
            if src in cycle:
                return False
            if src in seen:
                return True
            
            cycle.add(src)
            for prereq in adjList[src]:
                if not dfs(prereq):
                    return False
            cycle.remove(src)
            seen.add(src)
            
            res.append(src)
            
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []


        return res

        
        