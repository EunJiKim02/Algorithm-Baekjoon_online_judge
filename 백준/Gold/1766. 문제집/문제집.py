import heapq

class Graph:
    def __init__(self, v):
        self.v = v
        self.Node = [[]for _ in range(v+1)]
        self.reverse = [[]for _ in range(v+1)]

    def addNode(self, a, b):
        self.Node[a].append(b)
        self.reverse[b].append(a)

    def indegree(self, v):
        return len(self.reverse[v])
        


def topologicalSort(g):
    def bfs():
        while len(q) != 0:
            x = heapq.heappop(q)
            reverselist.append(x)
            for k in g.Node[x]:
                degree[k] -= 1
                if degree[k] == 0:
                    heapq.heappush(q, k)

    reverselist = []
    degree = [0 for _ in range(g.v+1)]
    q = []
    for i in range(1, g.v+1):
        degree[i] = g.indegree(i)
        if degree[i] == 0:
            heapq.heappush(q, i)
    
    bfs()
    return reverselist

    
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
g = Graph(N)
for _ in range(M):
    a, b = map(int, input().split())
    g.addNode(a, b)

ans = topologicalSort(g)
for x in ans:
    print(x, end=' ')