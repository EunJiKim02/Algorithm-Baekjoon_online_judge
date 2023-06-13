import heapq
import sys

input = sys.stdin.readline

pq = []
ans = []

N = int(input())

for _ in range(N):
    n, s, f = map(int, input().split())
    heapq.heappush(pq, (s, f))

while(len(pq) != 0):
    x = heapq.heappop(pq)
    if len(ans) == 0 :
        ans.append(x[1])
    else:
        m = min(ans)
        if m > x[0]:
            ans.append(x[1])    
        else:
            ans[ans.index(m)] = x[1]

print(len(ans))