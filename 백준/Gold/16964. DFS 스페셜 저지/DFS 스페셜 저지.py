import sys

class Graph:
  def __init__(self, V):
    self.v = V
    self.node = [[] for _ in range(V+1)]
  
  # undirected graph
  def addNode(self, a, b):
    self.node[a].append(b)
    self.node[b].append(a)

  def deleteNode(self, a, b):
    self.node[a].remove(b)
    self.node[b].remove(a)


class DFS:
  def __init__(self, graph, start, userinput):
    def dfsrecur(v):

      self.count += 1
      self.visited[v] = True
      while self.userindex < graph.v:
        x = userinput[self.userindex]
        if len(graph.node[v]) == 0 : return
        self.userindex += 1
        if x in graph.node[v]:

          if self.visited[x] == False:
            graph.deleteNode(v, x)
            dfsrecur(x)
          self.fromVertex[x] = v
        
    self.userindex = 1
    self.count = 0
    self.visited = [False for _ in range(graph.v+1)]
    self.fromVertex = [None for _ in range(graph.v+1)]
    dfsrecur(start)



if __name__ == '__main__':
  input = sys.stdin.readline
  N = int(input())
  g = Graph(N)
  for _ in range(N-1):
    a, b = map(int, input().split())
    g.addNode(a, b)
  


  p = list(map(int, input().split()))
  if p[0] != 1:
    print(0)
    exit(0)
  path = DFS(g, 1, p)


  if path.count == N:
    print(1)
  else: print(0)
    

    
