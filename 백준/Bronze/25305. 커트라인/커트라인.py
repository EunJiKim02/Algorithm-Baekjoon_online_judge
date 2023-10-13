k, n = map(int, input().split())
score = list(map(int, input().split()))

def insertionsortAndResult(a, n):
    for i, x in enumerate(a):
        for j in range(i-1, -1, -1):
            if a[j] >= x:
                break
            a[j+1], a[j] = a[j], a[j+1]
    return a[n-1]

print(insertionsortAndResult(score, n))
