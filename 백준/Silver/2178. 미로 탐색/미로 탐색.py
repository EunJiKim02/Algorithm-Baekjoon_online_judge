from collections import deque
n, m = map(int, input().split())

graph = []
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(n):
    graph.append(list(map(int, input())))

#시작점 방문
graph[0][0] = 0
q = deque([(0, 0)])
count = 1

while q:
    x, y = q.popleft()

    for mov in move:
        nx = x + mov[0]
        ny = y + mov[1]
        if(nx == n-1 and ny == m-1):
            print(graph[x][y] + 2)
            exit()
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            q.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
