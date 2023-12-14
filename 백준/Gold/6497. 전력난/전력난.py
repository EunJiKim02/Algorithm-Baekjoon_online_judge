import sys
input = sys.stdin.readline
from queue import PriorityQueue
#Kruskal

class UF:
  def __init__(self, N):
    self.size = [1 for _ in range(N)]
    self.idx = [i for i in range(N)]

  def root(self, i):
    while self.idx[i] != i: i = self.idx[i]
    return i
  
  def connected(self, a, b):
    return self.root(a) == self.root(b)
  
  def union(self, a, b):
    id1, id2 = self.root(a), self.root(b)
    if id1 == id2: return
    if self.size[id1] <= self.size[id2]:
      self.idx[id1] = id2
      self.size[id2] += self.size[id1]
    else:
      self.idx[id2] = id1
      self.size[id1] += self.size[id2]


if __name__== '__main__':
  while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
      break
    pq = PriorityQueue()
    wholeprice = 0
    for _ in range(n):
      x, y, z = map(int, input().split())
      wholeprice += z
      pq.put((z, x, y))

    price = 0
    result = []

    uf = UF(m)
    while not pq.empty():
      z, x, y = pq.get()
      if not uf.connected(x, y):
        uf.union(x, y)
        result.append((x, y, z))
        price += z
    print(wholeprice - price)