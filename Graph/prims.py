import queue
import sys

class Graph:

    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMat = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self,v1,v2,wt):
        self.adjMat[v1][v2] = wt
        self.adjMat[v2][v1] = wt

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
    
    def get_minVertex(self,visited,weight):
        min_vertex = -1
        for i in range(self.nVertices):
            if visited[i] is False and (min_vertex==-1 or weight[min_vertex] > weight[i]):
                min_vertex = i
        return min_vertex
    
    def prims(self):
        visited = [False for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]
        weight = [sys.maxsize for i in range(self.nVertices)]
        weight[0]=0

        for i in range(self.nVertices):
            min_vertex = self.get_minVertex(visited,weight)
            visited[min_vertex] = True

            for j in range(self.nVertices):
                if self.adjMat[min_vertex][j] > 0 and visited[j] is False:
                    if weight[j] > self.adjMat[min_vertex][j] :
                        weight[j] = self.adjMat[min_vertex][j]
                        parent[j] = min_vertex 
        
        for i in range(1,self.nVertices):
            if i > parent[i]:
                print("{} {} {}".format(parent[i],i,weight[i]))
            else:
                print("{} {} {}".format(i,parent[i],weight[i]))


li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]
g = Graph(n)

for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    g.addEdge(curr_input[0],curr_input[1],curr_input[2])
g.prims()