import sys
from queue import PriorityQueue
import math

input = sys.stdin.readline


class Edges:
  def __init__(self, v, w, weight):
    if v < w : self.v, self.w = v, w
    else: self.v, self.w = w, v
    self.weight = weight

  def __lt__(self, other):
    return self.weight < other.weight
  
  def __gt__(self, other):
    return self.weight > other.weight
  
  def __eq__(self, other):
    return self.weight == other.weight
  
  def other(self, v):
    if self.v == v: return self.w
    else: return self.v


class UF:
  def __init__(self, V):
    self.ids = [x for x in range(V)]
    self.size = [1 for _ in range(V)]
    
  def root(self, i):
    while self.ids[i] != i: i = self.ids[i]
    return i
  
  def connected(self, a, b):
    return self.root(a) == self.root(b)
  
  def union(self, a, b):
    id1, id2 = self.root(a), self.root(b)
    if id1 == id2: return
    if id1 <= id2:
      self.ids[id1] = id2
      self.size[id2] += self.size[id1]
    else:
      self.ids[id2] = id1
      self.size[id1] += self.size[id2]


class WDgraph:
  def __init__(self, V):
    self.V = V
    self.E = 0
    self.adj = [[]for _ in range(V)]
    self.edges = []

  def insert(self, v, w, weight):
    e = Edges(v, w, weight)
    self.adj[v].append(e)
    self.adj[w].append(e)
    self.E += 1
    self.edges.append(e)

def mstKruskal(g):
  mstedgeTo = []
  weightSum = 0

  pq = PriorityQueue()
  for e in g.edges:
    pq.put(e)

  uf = UF(g.V)

  while not pq.empty():
    e = pq.get()
    if not uf.connected(e.v, e.w):
      uf.union(e.v, e.w)
      mstedgeTo.append(e)
      weightSum += e.weight

  return mstedgeTo, weightSum

def getdistance(a, b):
  return math.sqrt( (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

if __name__ == '__main__':
  n = int(input())
  g = WDgraph(n)
  tmp = []
  for _ in range(n):
    x, y = map(float, input().split())
    tmp.append((x, y))

  for i in range(n):
    for j in range(i, n):
      v, w = i, j
      weight = getdistance(tmp[i], tmp[j])
      g.insert(v, w, weight)

  _, sum = mstKruskal(g)
  print(round(sum,2))
    