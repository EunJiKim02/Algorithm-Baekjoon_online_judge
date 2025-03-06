def nC2(n):
    return (n * (n-1)) //2

N, M = map(int, input().split())

num = list(map(int, input().split()))

remaining = [0 for _ in range(M)]
partial_sum = [0 for _ in range(N+1)]

for i in range(1, N+1):
    partial_sum[i] = partial_sum[i-1] + num[i-1]
    partial_sum[i] %= M
    remaining[partial_sum[i]]+=1


km = remaining[0]
ks = 0

for i in range(0, M):
    ks += nC2(remaining[i])

answer = km + ks
print(answer)