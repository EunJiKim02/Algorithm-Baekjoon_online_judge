from collections import deque
mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]
graph = []
m, n = map(int, input().split())

for _ in range(n):
    graph.append(list(map(int, input().split())))

q = deque()

# 여러개의 시작 노드 큐에 넣어주기
cnt = 0
for j in range(n):
    for i in range(m):
        if(graph[j][i] == 1):
            q.append((i, j))
            cnt += 1

if(cnt == m * n):
    print(0)
    exit()

result = 0
#토마토 탐색
while q:
    x, y = q.popleft()
    for move in mov:
        nx = move[0] + x
        ny = move[1] + y
        if 0<= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            result = max(result, graph[y][x])
            q.append((nx, ny))


cnt = 0
for j in range(n):
    for i in range(m):
        if(graph[j][i] != 0):
            cnt += 1

if(cnt == m * n):
    print(result)
    exit()
else:
    print("-1")
