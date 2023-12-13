import sys
from collections import deque
input = sys.stdin.readline

class topological:
  def __init__(self, N, g):
    self.g = g
    self.visited = [False for _ in range(N)]
    self.result  = []
    self.status = 0

    q = deque()
    for i in range(N):
      if g.indegree[i] == 0:
        q.append(i)
        g.indegree[i] -= 1

    for _ in range(N):
      if len(q) > 1:
        self.status = 1 # ?
        return
      if len(q) == 0:
        self.status = 2 # IMPOSSIBLE
        return
      
      x = q.popleft()
      self.result.append(x)
      for xt in g.adj[x]:
        k = xt.other(x)
        g.indegree[k] -= 1
        if g.indegree[k] == 0:
          q.append(k)

        


class WDGraph:
  class Edge:
    def __init__(self, v, w):
      if v < w: self.v, self.w = v, w
      else: self.v, self.w = w, v
    def other(self, v):
      if self.v == v: return self.w
      else: return self.v
    def __eq__(self, other):
      return(self.v == other.v) and (self.w == other.w)
    def __str__(self):
      return f'{self.v} -> {self.w}'
    def __repr__(self):
        return self.__str__()
        

  def __init__(self, N):
    self.V = N
    self.adj = [[]for _ in range(N)]
    self.indegree = [0 for _ in range(N)]
  
  def insert(self, v, w):
    e = self.Edge(v, w)
    self.adj[v].append(e)
    self.indegree[w] += 1

  def replace(self, a, b):
    e = self.Edge(a, b)
    if e in self.adj[a]:
      self.adj[a].remove(e)
      self.adj[b].append(e)
      self.indegree[b] -= 1
      self.indegree[a] += 1
    else:
      self.adj[b].remove(e)
      self.adj[a].append(e)
      self.indegree[a] -= 1
      self.indegree[b] += 1

if __name__ ==  '__main__':
  T = int(input())
  for _ in range(T):
    n = int(input())
    g = WDGraph(n)
    node = list(map(int, input().split()))

    # node 우선순위를 이용해 간선 연결
    for i in range(n):
      for j in range(i+1, n):
        g.insert(node[i]-1, node[j]-1)

    # 우선순위 수정
    m = int(input())
    for _ in range(m):
      a, b = map(int, input().split())
      g.replace(a-1, b-1)
    
    t = topological(n, g)
    result = t.result
    if t.status == 1:
      print('?')
    elif t.status == 2 :
      print('IMPOSSIBLE')
    else:
      for x in result:
        print(x+1, end=' ')
