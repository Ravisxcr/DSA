#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        arr = []
        q = Queue()
        visited = [False for i in range(V)]
        
        q.put(0)
        visited[0] = True
        
        while q.empty() is False:
            u = q.get()
            arr.append(u)
            
            for i in range(V):
                if adj[i][0] > 0 :
                    q.put(i)
                    visited[i] = True
        
        return arr


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
                    
		print()
        

# } Driver Code Ends