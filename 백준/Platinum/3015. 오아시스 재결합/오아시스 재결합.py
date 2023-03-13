import sys
input = sys.stdin.readline


n = int(input())
stack = []
result = 0

for x in range(n):
    k = int(input())
    while stack and stack[-1][0] < k:
        result += stack.pop()[1]

    if(stack and stack[-1][0] == k ):
        result += (stack[-1][1])
        if len(stack) != 1:
            result += 1
        stack[-1][1] += 1

    else:
        if stack:
            result += 1
        stack.append([k, 1])


print(result)
        
