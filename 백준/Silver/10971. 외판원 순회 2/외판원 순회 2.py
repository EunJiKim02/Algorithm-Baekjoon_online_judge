import sys
sys.setrecursionlimit(10**6)

# input
N = int(input())
W = []
MAX = sys.maxsize

for _ in range(N):
    W.append(list(map(int, input().split())))


def dfs(k, S):
    if len(S) == 0:
        if W[k][0] == 0:
            return MAX
        return W[k][0]
    minv = MAX
    for x in S:
        if W[k][x] == 0:
            continue
        r = S.copy()
        r.remove(x)
        minv = min(minv, dfs(x,r) + W[k][x])
    return minv

S = [x for x in range(N)]
S.remove(0)
print(dfs(0, S))
