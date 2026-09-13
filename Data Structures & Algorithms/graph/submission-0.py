class Graph:
    
    def __init__(self):
        self.adjList = defaultdict(lambda:[])


    def addEdge(self, src: int, dst: int) -> None:
        self.adjList[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            print("we removed " + str(dst) + " from " + str(src))
            print(self.adjList[src])
            return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        def dfs(src):
            print(src)
            if src in visit:
                return False
            if src == dst:
                return True
            
            visit.add(src)

            print(str(src)+ " neighbors: " + str(self.adjList[src]))
            for neighbor in self.adjList[src]:
                if dfs(neighbor):
                    return True            

            return False
        
        return dfs(src)
        
            


