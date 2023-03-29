
n, m = map(int, input().split())
arr = list(map(int, input().split()))

INF = 10001

cnt = [0 for _ in range(INF)]
arr.sort()
newarr = []
answer = []


for x in arr:
    if(cnt[x] == 0):
        newarr.append(x)
    cnt[x] += 1

nn = len(newarr)    
    
def backtracking(k):
    if len(answer) == m:
        for x in answer:
            print(x, end=' ')
        print()
        return
    for y in range(k, nn):
        answer.append(newarr[y])
        backtracking(y)
        answer.pop()

backtracking(0)
            