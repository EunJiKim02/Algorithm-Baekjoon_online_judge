from collections import deque
mov = [(1, 0, 0), (-1, 0, 0), 
       (0, 1, 0), (0, -1, 0),
       (0, 0, 1), (0, 0, -1)
       ]
m, n, h= map(int, input().split())

graph = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))

q = deque()

# 여러개의 시작 노드 큐에 넣어주기
cnt = 0
for k in range(h):
    for j in range(n):
        for i in range(m):
            if(graph[k][j][i] == 1):
                q.append((k, i, j))
                cnt += 1


result = 0
#토마토 탐색
while q:
    l, x, y = q.popleft()
    for move in mov:
        nl = move[0] + l
        nx = move[1] + x
        ny = move[2] + y
        if 0<= nx < m and 0 <= ny < n and 0 <= nl < h and graph[nl][ny][nx] == 0:
            graph[nl][ny][nx] = graph[l][y][x] + 1
            result = max(result, graph[l][y][x])
            q.append((nl, nx, ny))

cnt = 0
for k in range(h):
    for j in range(n):
        for i in range(m):
            if(graph[k][j][i] != 0):
                cnt += 1

if(cnt == m * n * h):
    print(result)
    exit()
else:
    print("-1")
