import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())

MAP = []

dp = [[-1 for _ in range(N)]for _ in range(M)]
for _ in range(M):
    MAP.append(list(map(int, input().split())))

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

dp[M-1][N-1] = 1
def dfs(i, j):
    if i == M-1 and j == N-1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 0
    for d in dir:
        nx = i + d[0]
        ny = j + d[1]
        if (nx < 0 or nx >= M) or (ny < 0 or ny >= N):
            continue
        if MAP[i][j] > MAP[nx][ny]:
            dp[i][j] += dfs(nx, ny)    
    return dp[i][j]

print(dfs(0, 0))