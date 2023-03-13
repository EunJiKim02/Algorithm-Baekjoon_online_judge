from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(a, b, graph):
  graph[a][b] = 0
  q = deque([(a, b)])
  while q:
    y, x = q.popleft()
    for move in mov:
      ny = move[0] + y
      nx = move[1] + x
      if ( 0 <= ny < n) and (0 <= nx < m) and graph[ny][nx]:
        q.append((ny, nx))
        graph[ny][nx] = 0



T = int(input())

#각 케이스에 대해 접근
for _ in range(T):
  m, n, k = map(int, input().split())
  count = 0
  graph = [[0 for _ in range(m)] for _ in range(n)]

  for _ in range(k):
    a, b = map(int, input().split())
    graph[b][a] = 1

  for i in range(n):
    for j in range(m):
      if(graph[i][j] == 1):
        bfs(i, j, graph)
        count += 1
  print(count)



