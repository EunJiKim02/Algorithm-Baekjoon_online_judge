from collections import deque
n, k = map(int, input().split())

arr = deque()
for i in range(1, n+1):
    arr.append(i)
print('<', end='')
while(True):
    for i in range(k):
        if(len(arr) == 0):
            break
        x = arr.popleft()
        if(i == k-1):
            print(f'{x}', end='')
            break
        arr.append(x)
    if(len(arr) == 0):
        break
    print(', ', end='')


print('>')