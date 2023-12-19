import sys
input = sys.stdin.readline

N, M= map(int,input().split())
arr = list(map(int, input().split()))
s = [0 for _ in range(N)]
s[0] = arr[0]
for i in range(1, N):
    s[i] = s[i-1] + arr[i]
for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(s[j-1])
    else:
        print(s[j-1] - s[i-2])