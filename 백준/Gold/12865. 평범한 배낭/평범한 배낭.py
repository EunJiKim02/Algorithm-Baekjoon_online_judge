n, k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
knapsack = [(0,0)]

for _ in range(n):
    a, b = map(int, input().split())
    knapsack.append((a, b))

for i in range(1, n+1):
    for j in range(1, k+1):
        if knapsack[i][0] >j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][max(0, j - knapsack[i][0])]+knapsack[i][1])
          
print(dp[n][k])