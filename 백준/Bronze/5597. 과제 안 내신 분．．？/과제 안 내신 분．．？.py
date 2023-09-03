N = 30
arr = [False for _ in range(N+1)]

for _ in range(N-2):
    n = int(input())
    arr[n] = True

for i in range(1, N+1):
    if not arr[i]:
        print(i)