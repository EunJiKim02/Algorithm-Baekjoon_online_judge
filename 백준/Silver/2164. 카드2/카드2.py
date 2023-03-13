from collections import deque
n = int(input())
k = deque()

for i in range(1, n+1):
    k.append(i)

while(True):
    if len(k) == 1:
      print(k.popleft())
      break
    k.popleft()
    n = k.popleft()
    k.append(n)
