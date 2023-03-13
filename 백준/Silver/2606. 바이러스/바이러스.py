from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[]for _ in range(n+1)]

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
q = deque([1])

visited = [False] * (n+1)
visited[1] = True

while q:
    f = q.popleft()
    for x in graph[f]:
        if not visited[x]:
            cnt += 1
            q.append(x)
            visited[x] = True


print(cnt)