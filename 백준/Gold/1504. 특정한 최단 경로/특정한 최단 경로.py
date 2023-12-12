import sys
from queue import PriorityQueue
input = sys.stdin.readline

class WUGraph:
  class Edge:
    def __init__(self, v, w, weight):
      self.v, self.w, self.weight = v, w, weight

    def other(self, v):
      if self.v == v : return self.w
      else: return self.v

  def __init__(self, V):
    self.V = V
    self.adj = [[]for _ in range(V)]

  def insert(self, v, w, weight):
    e = self.Edge(v, w, weight)
    self.adj[v].append(e)
    self.adj[w].append(e)


class ShortestPath:
  def __init__(self, g, s):
    self.g, self.s = g, s
    self.distTo = [float('inf') for _ in range(g.V)]
    self.distTo[s] = 0
    self.ShortestPath()

  def ShortestPath(self):
    visited = [False for _ in range(self.g.V)]

    visitcount = 1
    pq = PriorityQueue() # weight, s
    
    # 시작점 정점 넣기
    
    pq.put((0, self.s))

    while not pq.empty() and visitcount < self.g.V:
      dist, k = pq.get()
      if visited[k]:
        continue
      visited[k] = True
      visitcount += 1

      for e in self.g.adj[k]:
        if dist + e.weight < self.distTo[e.other(k)]:
          self.distTo[e.other(k)] = dist + e.weight
        pq.put((self.distTo[e.other(k)], e.other(k)))
    


if __name__ == '__main__':
  N, E = map(int, input().split())
  g = WUGraph(N)
  for _ in range(E):
    a, b, c, = map(int, input().split())
    g.insert(a-1, b-1, c)

  u, v = map(int, input().split())

  sp1 = ShortestPath(g, 0)
  spu = ShortestPath(g, u-1)
  spv = ShortestPath(g, v-1)

  sp1ToU = sp1.distTo[u-1]
  sp1ToV = sp1.distTo[v-1]

  spUToV = spu.distTo[v-1]
  spUToN = spu.distTo[N-1]

  spVToU = spv.distTo[u-1]
  spVToN = spv.distTo[N-1]

  ans = min(sp1ToU + spUToV + spVToN, sp1ToV + spVToU + spUToN)

  if ans == float('inf'):
    print(-1)
  else:
    print(ans)

