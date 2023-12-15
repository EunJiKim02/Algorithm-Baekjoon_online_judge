import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
x = set(map(int, input().split()))
M = int(input())
e = list(map(int, input().split()))
for k in e:
    if k in x:
        print(1)
    else:
        print(0)

        