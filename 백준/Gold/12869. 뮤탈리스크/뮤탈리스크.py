import sys
import math
sys.setrecursionlimit(10**6)
INF = sys.maxsize
SIZE = 61

N = int(input())
health = [0,0,0]
dp = [[[0 for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(SIZE)]

k = list(map(int, input().split()))
for i in range(N):
    health[i] = k[i]

RESULT = INF

def count(x, y, z, cnt):
    global RESULT
    # end condition
    if x <= 0 and y <= 0 and z <=0:
        RESULT = min(RESULT, cnt)
        return
    
    x = max(0, x)
    y = max(0, y)
    z = max(0, z)

    if cnt >= dp[x][y][z] and dp[x][y][z] != 0 :
        return
    
    # RESULT update
    dp[x][y][z] = cnt

    # recursion
    count(x-9, y-3, z-1, cnt+1)
    count(x-9, y-1, z-3, cnt+1)
    count(x-3, y-1, z-9, cnt+1)
    count(x-3, y-9, z-1, cnt+1)
    count(x-1, y-9, z-3, cnt+1)
    count(x-1, y-3, z-9, cnt+1)



count(health[0], health[1], health[2], 0)
print(RESULT)