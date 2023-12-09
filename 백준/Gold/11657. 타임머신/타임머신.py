import sys
input = sys.stdin.readline

class Edges:
  def __init__(self, v, w, weight):
    self.v, self.w = v,w
    self.weight = weight

  def __lt__(self, other):
    return self.weight < other.weight
  
  def __gt__(self, other):
    return self.weight > other.weight
  
  def __eq__(self, other):
    return self.weight == other.weight

class WDgraph:
  def __init__(self, v):
    self.V = v
    self.E = 0
    self.adj = [[]for _ in range(v)]
    self.edges = []

  def insert(self, v, w, weight):
    e = Edges(v, w, weight)
    self.adj[v].append(e)
    self.E += 1
    self.edges.append(e)

class SP:
  def __init__(self, g, s): # s : 출발점
    self.g, self.s = g, s
    self.edgeTo = [None for _ in range(g.V)]
    self.distTo = [float('inf') for _ in range(g.V)]
    self.distTo[s] = 0

  def pathTo(self, v):
    path = []
    e = self.edgeTo[v]
    while e != None:
      path.append(e)
      e = self.edgeTo[e.v]
    path.reverse()
    return path
  
  def hasPathTo(self, v):
    return self.distTo[v] < float('inf')

  def relax(self, e):
    if self.distTo[e.w] > self.distTo[e.v] + e.weight:
      self.distTo[e.w] = self.distTo[e.v] + e.weight
      self.edgeTo[e.w] = e
      return True

if __name__ == '__main__':
  N, M = map(int, input().split())
  g = WDgraph(N)
  for _ in range(M):
    v, w, weight = map(int, input().split())
    g.insert(v-1, w-1, weight)

  sp = SP(g, 0)
  for _ in range(g.V-1):
    for v in range(g.V):
      for e in g.adj[v]:
        sp.relax(e)
        #print(e.v, e.w,e.weight, sp.distTo)
  
  for v in range(g.V):
    for e in g.adj[v]:
      if sp.relax(e):
        print(-1)
        sys.exit()

  time = sp.distTo
  
  for x in time[1:]:
    if x == float('inf'):
      print(-1)
    else:
      print(x)