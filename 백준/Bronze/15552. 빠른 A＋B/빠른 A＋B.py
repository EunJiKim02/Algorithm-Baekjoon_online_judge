import sys

n = int(sys.stdin.readline().rstrip())
list1 = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    list1.append(a+b)

for i in range(n):
    print(list1[i])
