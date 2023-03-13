from collections import deque
mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]
wallbreak = [(2, 0), (-2, 0), (0, -2), (0, 2), (1, -1), (-1, 1), (1, 1), (-1, -1)]
n, m = map(int, input().split())

graph = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input())))

#(x, y, isBreak)
q = deque([(0, 0, 0)])
visited[0][0][0] = 1

while q:
    x, y, isBreak = q.popleft()
    for mo in mov:
        nx = x + mo[0]
        ny = y + mo[1]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and visited[nx][ny][isBreak] == 0:
            q.append((nx, ny, isBreak))
            visited[nx][ny][isBreak] = visited[x][y][isBreak] + 1
        elif not isBreak and 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            q.append((nx, ny, 1))
            visited[nx][ny][1] = visited[x][y][0] + 1


if(visited[n-1][m-1][0] == 0 and visited[n-1][m-1][1] == 0):
    print(-1)
else:
    if(visited[n-1][m-1][0] == 0):
        print(visited[n-1][m-1][1])
    elif(visited[n-1][m-1][1] == 0):
        print(visited[n-1][m-1][0])
    else:
        print(min(visited[n-1][m-1][0], visited[n-1][m-1][1]))