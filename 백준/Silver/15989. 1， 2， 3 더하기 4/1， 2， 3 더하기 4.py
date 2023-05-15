T = int(input())


k = []
    
for _ in range(T):
    k.append(int(input()))

MAX = max(k)
dp = [[0,0,0] for _ in range(MAX+1)]
dp[1][0] = 1
dp[1][1] = 0
dp[1][2] = 0
dp[2][0] = 1
dp[2][1] = 1
dp[2][2] = 0
dp[3][0] = 2
dp[3][1] = 0
dp[3][2] = 1

for x in range(4, MAX+1):
    dp[x][0] = sum(dp[x-1])
    dp[x][1] = dp[x-2][1] + dp[x-2][2]
    dp[x][2] = dp[x-3][2]

for x in k:
    print(sum(dp[x]))
    