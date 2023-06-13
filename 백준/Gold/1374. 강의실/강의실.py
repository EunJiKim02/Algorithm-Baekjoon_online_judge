import heapq
import sys

input = sys.stdin.readline

pq = []
ans = []
arr = []

N = int(input())
pq = []

for i in range(N):
    n, s, f = map(int, input().split())
    arr.append([s, f])

arr.sort()
heapq.heappush(pq, arr[0][1])

for i in range(1, N):
    if pq[0] > arr[i][0]:
        heapq.heappush(pq,arr[i][1])
    else:
        heapq.heappop(pq)
        heapq.heappush(pq,arr[i][1])
print(len(pq))