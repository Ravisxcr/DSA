from graph import Edge

def getParent(v,parent):
    if v==parent[v]:
        return v
    return getParent(parent[v],parent)

def krushkal(edges, nVertices):
    parent = [i for i in range(nVertices)]
    edges = sorted(edges, key = lambda edge:edge.wt)
    count = 0
    output = []
    i = 0
    
    while count < (nVertices - 1):
        currentEdge = edges[i]
        srcParent = getParent(currentEdge.src, parent)
        destParent = getParent(currentEdge.dst, parent)

        if srcParent != destParent:
            output.append(currentEdge)
            count+=1
            parent[srcParent] = destParent
        i+=1
    return output


li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]
edges = []

for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    wt = curr_input[2]
    edge = Edge(src,dest,wt)
    edges.append(edge)
output = krushkal(edges,n)

for edge in output:
    if edge.src < edge.dst:
        print(str(edge.src)+" "+str(edge.dst)+" "+str(edge.wt))
    else:
        print(str(edge.dst)+" "+str(edge.src)+" "+str(edge.wt))