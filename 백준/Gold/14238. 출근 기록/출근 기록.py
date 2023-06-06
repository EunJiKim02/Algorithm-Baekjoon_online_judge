import sys
sys.setrecursionlimit(10 ** 6)

C = 2
B = 1
A = 0

S = list(input())
numA = S.count('A') 
numB = S.count('B') 
numC = S.count('C') 

MAX = 51

val = ['A', 'B', 'C']

dp = [[[[[0, 0, 0] for _ in range(3)]  for _ in range(MAX)] for _ in range(MAX)]for _ in range(MAX)]
ans = [0 for _ in range(len(S))]

def dfs(a, b, c, l2, l1):
    
    if a == numA and b == numB and c == numC:
        return 1
    
    if dp[a][b][c][l2][l1] == 1:
        return 0
    dp[a][b][c][l2][l1] = 1
    if a < numA :
        if dfs(a+1, b, c, l1, A) == 1:
            ans[a+b+c] = val[A]
            return 1
    if b < numB and  l1 != B:
        if dfs(a, b+1, c, l1, B) == 1:
            ans[a+b+c] = val[B]
            return 1
    if c < numC and l2 != C and l1 != C:
        if dfs(a, b, c+1, l1, C) == 1:
            ans[a+b+c] = val[C]
            return 1
        
    return 0

    
dfs(0, 0, 0, A, A)
    
if ans[0] == 0:
    print(-1)
else:
    for x in ans:
        print(x, end='')