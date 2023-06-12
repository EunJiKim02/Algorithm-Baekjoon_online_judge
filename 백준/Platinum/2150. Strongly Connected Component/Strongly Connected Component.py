import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

VISIT = 0; NOTVISIT = -1

V, E = map(int, input().split())

G = [[] for _ in range(V+1)]
visited = [NOTVISIT for _ in range(V+1)]
stack = []
answer = []
cnt = 0


# graph input
for _ in range(E):
    A, B = map(int, input().split())
    G[A].append(B)



def dfs(n):
    global cnt
    cnt += 1
    visited[n] = cnt
    stack.append(n)

    p = visited[n]
    for x in G[n]:
        if visited[x] == NOTVISIT:
            p = min(p, dfs(x))
        elif visited[x] != VISIT:
            p = min(p, visited[x])
    if p == visited[n]:
        temp = []
        while(1):
            t = stack[-1]
            temp.append(t)
            stack.pop()
            visited[t] = VISIT
            if t == n:
                break
        temp.sort()
        answer.append(temp)
            
    return p


for i in range(1, V+1):
    # 이미 방문했다면 넘어감
    if visited[i] == NOTVISIT:
        dfs(i)

print(len(answer))
answer.sort()
for k in answer:
    for l in k:
        print(l, end = ' ')
    print(-1)
        
    
    
    
    
