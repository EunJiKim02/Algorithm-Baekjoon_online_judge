from collections import deque


n, m = map(int, input().split())
d = deque(range(1, n+1))
ans = list(map(int, input().split()))

cnt = 0

for x in ans:
    if(x == d[0]):
      d.popleft()
      continue
    #왼쪽이 더 먼 경우
    if d.index(x) > (len(d) // 2):
        while(True):
          if(x == d[0]):
            d.popleft()
            break
          cnt += 1
          k = d.pop()
          d.appendleft(k)
    else:
        while(True):
          if(x == d[0]):
            d.popleft()
            break
          cnt += 1
          k = d.popleft()
          d.append(k)

print(cnt)