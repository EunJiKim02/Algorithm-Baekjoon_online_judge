import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    q = input()
    s = int(q[0])
    if s == 1:
        _, x = map(int, q.split())
        stack.append(x)
    elif s == 2:
        if len(stack) == 0:
            print(-1)
        else:
            x = stack.pop()
            print(x)
    elif s == 3:
        print(len(stack))
    elif s == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        