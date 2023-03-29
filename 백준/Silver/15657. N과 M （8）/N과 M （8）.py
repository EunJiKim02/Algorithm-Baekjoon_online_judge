n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []

def findmax(k):
    if len(answer) == m:
        for x in answer:
            print(x, end=' ')
        print()
        return
    for x in range(k, n):
        answer.append(arr[x])
        findmax(x)
        answer.pop()

findmax(0)