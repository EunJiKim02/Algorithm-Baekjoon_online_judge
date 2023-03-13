from collections import deque

mov = [(1, 2), (-1, 2), (-1, -2), (1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

n = int(input())

def bfs(start, end, graph, l):
    q = deque([start])
    graph[start[0]][start[1]] = 1
    while q:
        f = q.popleft()
        for m in mov:
            nx = m[0] + f[0]
            ny = m[1] + f[1]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                if(nx == end[0] and ny == end[1]):
                    return graph[f[0]][f[1]]
                graph[nx][ny] = graph[f[0]][f[1]] + 1
                q.append((nx, ny))
    return 0


for _ in range(n):
    l = int(input())
    chess = [[0 for _ in range(l)] for _ in range(l)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(bfs(start, end, chess, l))

