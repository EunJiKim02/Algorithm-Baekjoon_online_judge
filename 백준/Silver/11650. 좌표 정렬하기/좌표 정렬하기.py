import sys

input = sys.stdin.readline

n = int(input())

point = []
for _ in range(n):
    a, b = map(int, input().split())
    point.append((a, b))
    
point.sort()

for x in point:
    print(x[0], x[1])