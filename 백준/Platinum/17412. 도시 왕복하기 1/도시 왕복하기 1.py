import sys
input = sys.stdin.readline

from queue import Queue

class FlowEdge:
  def __init__(self, v, w, capacity):
    self.v, self.w, self.capacity = v, w, capacity
    self.flow = 0.0

  def other(self, vertex):
    if self.v == vertex: return self.w
    elif self.w == vertex: return self.v

  def remainingCapacityTo(self, vertex):
    if vertex == self.v: return self.flow
    elif vertex == self.w: return self.capacity - self.flow

  def addRemainingCapacityTo(self, vertex, delta):
    if vertex == self.v: self.flow -= delta
    elif vertex == self.w: self.flow += delta

class FlowNetwork:
  def __init__(self, V):
    self.V = V
    self.E = 0
    self.adj = [[]for _ in range(V)]

  def addEdge(self, e):
    self.adj[e.v].append(e) # forward
    self.adj[e.w].append(e) # backward
    self.E += 1

class FordFulkerson:
  def __init__(self, g, s, t):
    self.g, self.s, self.t = g, s, t
    self.flow = 0
    while self.hasAugmentingPath():
      minflow = float('inf')
      v = t
      while v != s:
        minflow = min(minflow, self.edgeTo[v].remainingCapacityTo(v))
        v = self.edgeTo[v].other(v)

      v = t
      while v != s:
        self.edgeTo[v].addRemainingCapacityTo(v, minflow)
        v = self.edgeTo[v].other(v) # 간선 따라감

      self.flow += minflow

  def hasAugmentingPath(self):
    self.edgeTo = [None for _ in range(self.g.V)]
    self.visited = [False for _ in range(self.g.V)]

    q = Queue()
    q.put(self.s)
    while not q.empty():
      v = q.get()
      for e in g.adj[v]:
        w = e.other(v)
        if e.remainingCapacityTo(w) > 0 and not self.visited[w]:
          self.edgeTo[w] = e
          self.visited[w] = True
          q.put(w)

    return self.visited[self.t]


if __name__ == '__main__':
  N, P = map(int, input().split())
  g = FlowNetwork(N)
  for _ in range(P):
    v, w = map(int, input().split())
    e = FlowEdge(v-1, w-1, 1)
    g.addEdge(e)

  ff = FordFulkerson(g, 0, 1)
  print(int(ff.flow))