import sys
a = [0 for _ in range(10001)]
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    a[k] += 1

for i in range(1, 10001):
    repeat = a[i]
    for _ in range(repeat):
        print(i)
    
