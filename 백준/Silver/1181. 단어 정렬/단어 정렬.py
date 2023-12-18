import sys
input = sys.stdin.readline
n = int(input())

arr = []
for _ in range(n):
    s = input()
    if (len(s), s) not in arr:
        arr.append((len(s), s))
    
arr.sort()

for x in arr:
    print(x[1], end='')