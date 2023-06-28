import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input())

count = 0

def dfs(n, flight, visited):
    global count
    visited[n] = True
    count += 1
    for k in flight[n]:
        if visited[k] == False:
            dfs(k, flight, visited)


for _ in range(T):
    N, M = map(int, input().split())
    flight = [[] for k in range(N+1)]
    visited = [False for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        flight[a].append(b)
    count = 0
    for i in range(1, N+1):
        if visited[i] == False:
            dfs(i, flight, visited)
    print(count-1)
    flight.clear()
    visited.clear()