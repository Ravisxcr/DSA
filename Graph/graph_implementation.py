from graph import Graph

q = Graph(5)

q.addEdge(0,1)
q.addEdge(0,2)
q.addEdge(3,4)
print(q)

q.dfs()
q.bfs()