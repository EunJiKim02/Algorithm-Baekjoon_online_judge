from queue import PriorityQueue
import sys
input = sys.stdin.readline

class Edge:
  def __init__(self, a, b, w):
    if a <=b : self.v, self.w = a, b
    else: self.v, self.w = b, a
    self.weight = w

  def other(self, v):
    if self.v == v: return self.w
    else: return self.v

  def __lt__(self, other):
    return self.weight < other.weight

  def __gt__(self, other):
    return self.weight > other.weight
    
  def __eq__(self, other):
    return self.weight == other.weight

class UF:
  def __init__(self, x):
    
    self.idx = [k for k in range(x)]
    self.size = [1 for _ in range(x)]

  def root(self, a):
    while a != self.idx[a]:
      a = self.idx[a]
    return a
  
  def connect(self, a, b):
    return self.root(a) == self.root(b)
  
  def union(self, a, b):
    id1, id2 = self.root(a), self.root(b)
    if id1 == id2:  return
    if self.size[id1] <= self.size[id2]:
      self.idx[id1] = id2
      self.size[id2] += self.size[id1]
    else:
      self.idx[id2] = id1
      self.size[id1] += self.size[id2]


class graph:
  def __init__(self, v):
    self.E = 0 # number of edges
    self.V = v # number of vertex
    self.adj = [[] for _ in range(v)]
    self.edges = []
    
  def insert(self, a, b, w):
    e = Edge(a, b, w)
    self.adj[a].append(e)
    self.adj[b].append(e)
    self.edges.append(e)
    self.E += 1
    
def mstKruskal(g):
  edgesInMST = []
  weightSum = 0
  pq = PriorityQueue()
  for e in g.edges:
    pq.put(e)

  uf = UF(g.V+1)

  while not pq.empty():
    e = pq.get()
    if not uf.connect(e.v, e.w):
      uf.union(e.v, e.w)
      edgesInMST.append(e)
      weightSum += e.weight

  return edgesInMST, weightSum


if __name__ == '__main__':
  V, E = map(int, input().split())
  g = graph(V+1)

  for _ in range(E):
    a, b, w = map(int, input().split())
    g.insert(a, b, w)

  edges, weightSum = mstKruskal(g)
  print(weightSum)
