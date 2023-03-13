from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[]for _ in range(n+1)]
visited = [0] * (n+1)
q = deque()
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


cnt = 1

visited[r] = cnt
q.append(r)
while q:
    f = q.popleft()
    graph[f].sort(reverse=True)
    for i in graph[f]:
        if visited[i] == 0:
            q.append(i)
            cnt += 1
            visited[i] = cnt

for i in visited[1:]:
    print(i)