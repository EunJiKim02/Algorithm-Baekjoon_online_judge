import sys
input = sys.stdin.readline


class WDgraph:
  class Edge:
    def __init__(self, v, w, weight):
      self.v, self.w, self.weight = v, w, weight

  def __init__(self, N):
    self.V = N
    self.adj = [[]for _ in range(N)]
  
  def insert(self, v, w, weight):
    e = self.Edge(v, w, weight)
    self.adj[v].append(e)

def BellmanFord(g):
  distTo = [0 for _ in range(g.V)]
  for k in range(g.V):
    for i in range(g.V):
      for e in g.adj[i]:
        if distTo[e.w] > distTo[e.v] + e.weight:
          distTo[e.w] = distTo[e.v] + e.weight
          if distTo[e.w] < 0 and (k == g.V-1):
            return True
  return False

if __name__ == '__main__':
  T = int(input())
  for _ in range(T):
    N, M, W = map(int, input().split()) 
    g = WDgraph(N) 
    for _ in range(M):
      s, e, t = map(int, input().split())
      g.insert(e-1, s-1, t)
      g.insert(s-1, e-1, t)

    for _ in range(W):
      s, e, t = map(int, input().split())
      g.insert(s-1, e-1, t * -1)

    if BellmanFord(g):
      print('YES')
    else:
      print('NO')
