
n, m = map(int, input().split())
arr = list(map(int, input().split()))

INF = 10001

cnt = [0 for _ in range(INF)]
visited = [0 for _ in range(INF)]
arr.sort()
newarr = []
answer = []


for x in arr:
    if(cnt[x] == 0):
        newarr.append(x)
    cnt[x] += 1
    
    
def backtracking():
    if len(answer) == m:
        for x in answer:
            print(x, end=' ')
        print()
        return
    for y in newarr:
        if cnt[y] > visited[y]:
            answer.append(y)
            visited[y] += 1
            backtracking()
            answer.pop()
            visited[y] -= 1

backtracking()
            