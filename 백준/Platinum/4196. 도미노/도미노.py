
from queue import Queue

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


'''
Class for storing directed graphs
'''
class Digraph:
    def __init__(self, V): # Constructor
        self.V = V # Number of vertices
        self.E = 0 # Number of edges
        self.adj = [[] for _ in range(V)]   # adj[v] is a list of vertices pointed from v

    def addEdge(self, v, w): # Add a directed edge v->w. Self-loops and parallel edges are allowed
        self.adj[v].append(w)        
        self.E += 1

    def outDegree(self, v):
        return len(self.adj[v])

    def __str__(self):
        rtList = [f"{self.V} vertices and {self.E} edges\n"]
        for v in range(self.V):
            for w in self.adj[v]:
                rtList.append(f"{v}->{w}\n")
        return "".join(rtList)        

    def reverse(self): # return a digraph with all edges reversed
        g = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj[v]: g.addEdge(w, v)
        return g


'''
Perform the topological sort on a DAG g, and return list of vertices in reverse DFS postorder
'''
def topologicalSort(g):
    def recur(v):        
        visited[v] = True        
        for w in g.adj[v]:            
            if not visited[w]: recur(w)
        reverseList.append(v)            

    assert(isinstance(g, Digraph))
    visited = [False for _ in range(g.V)]
    reverseList = []
    for v in range(g.V): 
        if not visited[v]: recur(v)

    reverseList.reverse()
    return reverseList

'''
Class that finds SCC (Strongly-Connected Components) and stores the results    
'''
class SCC:
    def __init__(self, g):
        def recur(v): # DFS to mark all vertices connected to v            
            self.id[v] = self.count
            for w in g.adj[v]:
                if self.id[w] < 0: 
                    recur(w)                            
        self.g = g
        self.id = [-1 for i in range(g.V)] # id[v] is the ID of component to which v 
        self.count = 0 
        a = topologicalSort(g)
        for v in a:
            if self.id[v] < 0:
                recur(v)
                self.count += 1        

    def connected(self, v, w): 
        return self.id[v] == self.id[w]       




if __name__ == "__main__":
    T = int(input())
    answer = 0
    for _ in range(T):
        N, M = map(int, input().split())
        visited = [False for _ in range(N)]
        g1 = Digraph(N)
        for _ in range(M):
            x, y = map(int, input().split())
            g1.addEdge(x-1, y-1)
        #a = topologicalSort(g1)
        scc = SCC(g1)
        print(scc.count)
        


    
