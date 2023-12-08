import sys
input = sys.stdin.readline

class graph:
  def __init__(self, v):
    self.V = [[] for _ in range(v+1)]
    self.root = None

  def append(self, a, b):
    self.V[b].append(a)

  def len(self, a):
    return len(self.V[a])

  def LCA(self, s1, s2):
    from collections import deque
    s1result = {}
    s2result = {}
    
    q = deque()
    q.appendleft((s1, 1, 0))
    q.appendleft((s2, 2, 0))
    while(len(q)!=0):
      x, k, d = q.pop()
      if k == 1:
        if x not in s1result:
          s1result[x] = d
        if x in s2result:
          return x 
        for n in self.V[x]:
          if n not in s1result:
            q.append((n, 1, d+1))
      else:
        if x not in s2result:
          s2result[x] = d
        if x in s1result:
          return x
        for n in self.V[x]:
          if n not in s2result:
            q.append((n, 2, d+1))

if __name__ == '__main__':
  T = int(input())
  for _ in range(T):
    N = int(input())
    g = graph(N)
    for _ in range(N-1):
      a, b = map(int, input().split())
      g.append(a, b)
    s1, s2 = map(int, input().split())
    d = g.LCA(s1, s2)
    print(d)

