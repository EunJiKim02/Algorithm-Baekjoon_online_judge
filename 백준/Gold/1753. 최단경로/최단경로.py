import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
INF = sys.maxsize

graph = [[] for _ in range(V+1)]
path = [INF for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
q = []
# dijkstar
path[k] = 0
# queue (가중치, k에서 부터의 목적지)
heapq.heappush(q, (0, k)) # 맨 앞 요소로 priority queue 작동
while q:
    nw, nd = heapq.heappop(q)
    if nw > path[nd]:
        continue
    for x in graph[nd]:
        if nw + x[1] < path[x[0]]:
            path[x[0]] = nw + x[1]
            heapq.heappush(q, (path[x[0]],x[0]))


for x in path[1:]:
    if x == INF:
        print('INF')
    else:
        print(x)

