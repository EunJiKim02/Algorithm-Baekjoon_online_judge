import sys
import os
input = sys.stdin.readline


N = int(input())

arr = []
for i in range(N):
    k = int(input())
    arr.append((k, i))

arr.sort()
#print(arr)
ans = 0
for i, x in enumerate(arr):
    diff = x[1] - i
    ans = max(ans, diff)

print(ans + 1)