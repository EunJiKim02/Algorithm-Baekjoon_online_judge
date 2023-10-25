x = [1,1,2,2,2,8]
arr = list(map(int, input().split()))

for i in range(6):
    x[i] -= arr[i]

for t in x:
    print(t, end=' ')