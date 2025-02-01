
N, S = map(int,input().split())

arr = list(map(int, input().split()))

start, end = 0, 0
sum = arr[0]

ans = 1000001

while True:
    if start > end:
        break
    if sum < S:
        end += 1
        if end >= N:
            break
        sum += arr[end]
    else:
        sum -= arr[start]
        ans = min(ans, end-start+1)
        start += 1

if ans < 100000:
    print(ans)
else:
    print(0)
