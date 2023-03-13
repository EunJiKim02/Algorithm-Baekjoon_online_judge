from collections import deque

MAX = 100001
#(a, b) -> a * x + b
mov = [(1, -1), (1, 1), (2, 0)]

n, k = map(int, input().split())
visited = [0 for _ in range(MAX)]

q = deque()
q.append(n)
while q:
    f = q.popleft()
    if f == k:
        print(visited[f])
        break
    for m in mov:
        nx = m[0] * f + m[1]
        if 0 <= nx < MAX and visited[nx] == 0:
            if(nx == k):
                print(visited[f] + 1)
                exit()
            q.append(nx)
            visited[nx] = visited[f] + 1
