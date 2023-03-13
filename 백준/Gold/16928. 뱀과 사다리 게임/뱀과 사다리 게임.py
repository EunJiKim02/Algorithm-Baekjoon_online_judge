from collections import deque

dice = [1, 2, 3, 4, 5, 6]
graph = [0 for _ in range(101)]

n, m = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    graph[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    graph[u] = v

q = deque([(1, 1) ])

while q:
    f, cnt = q.popleft()
    for d in dice:
        np = f + d
        if(np < 100 and graph[np] != -1):
            if(graph[np]!= 0):
                np = graph[np]
            q.append((np, cnt + 1))
            graph[f] = -1
        elif(np == 100):
            print(cnt)
            exit()
