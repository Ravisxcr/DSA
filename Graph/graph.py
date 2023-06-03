import queue
class Graph:

    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMat = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self,v1,v2):
        self.adjMat[v1][v2] = 1
        self.adjMat[v2][v1] = 1

    def containsEdge(self,v1,v2):
        return True if self.adjMat[v1][v2] > 0 else False
    
    def __dfsHelper(self,sv,visited):

        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if (self.adjMat[sv][i] > 0 and visited[i] is False):
                self.__dfsHelper(i,visited)
    
    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                print(f"Exploring DFS through {i}")
                self.__dfsHelper(i,visited)

    def __bfsHelper(self,sv,visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            u = q.get()
            print(u)
            for i in range(self.nVertices):
                if self.adjMat[u][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited = [False for _ in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                print(f"Exploring BFS from {i}")
                self.__bfsHelper(i,visited)

    def removeEdge(self, v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMat[v1][v2] = 0
        self.adjMat[v2][v1] = 0

    def __str__(self):
        return str(self.adjMat)
    
class Edge:
    def __init__(self,src,dst,wt):
        self.src = src
        self.dst = dst
        self.wt = wt