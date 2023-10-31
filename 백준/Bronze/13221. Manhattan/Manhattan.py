import sys
input = sys.stdin.readline
mypoint = list(map(int, input().split()))
k = int(input())
taxi = []
for _ in range(k):
    a, b = map(int, input().split())
    d = abs(a - mypoint[0])
    d += abs(b - mypoint[1])
    taxi.append((d, a, b))

taxi.sort()
print(taxi[0][1], taxi[0][2])