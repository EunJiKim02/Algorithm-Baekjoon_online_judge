from collections import deque
import sys


mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j, graph):
    count = 1
    graph[i][j] = 0
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for mm in mov:
            nx = x + mm[0]
            ny = y + mm[1]
            if(0 <= nx < n and 0 <= ny < n and graph[nx][ny]):
                count += 1
                q.append((nx, ny))
                graph[nx][ny] = 0
    return count
        


n = int(input())

graph = []
count = []

for _ in range(n):
    graph.append(list(map(int,input())))

for i in range(n):
    for j in range(n):
        if(graph[i][j] == 1):
            count.append(bfs(i, j, graph))

print(len(count))
count.sort()
for c in count:
    print(c)

