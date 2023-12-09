
class Tree:
  def __init__(self, v):
    self.size = v
    self.adj = [[] for _ in range(v)]

  def insert(self, v, w, weight):
    self.adj[v].append((w, weight))


  def getdiameter(self):
    def dfs(v, x, s):
      for i in self.adj[x]:
        w, weight = i[0], i[1]
        if v[w] == 0:
          v[w] = s+weight
          dfs(v, w,s+weight)

    visited = [0 for _ in range(self.size)]
    visited[0] = -1
    dfs(visited, 0, 0)
    a = visited.index(max(visited))

    visited = [0 for _ in range(self.size)]
    visited[a] = -1
    dfs(visited, a, 0)
    return max(visited)
    
import sys
input = sys.stdin.readline

if __name__ == '__main__':
  V = int(input())
  t = Tree(V)
  for _ in range(V):
    k = list(map(int, input().split()))
    k.pop()
    a = k[0]-1
    for i in range(1, len(k), 2):
      b, w = k[i]-1, k[i+1]
      t.insert(a, b, w)

  d = t.getdiameter()
  print(d)
    
      
    
