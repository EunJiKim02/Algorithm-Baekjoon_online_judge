import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

ids = [x for x in range(N+1)]
size = [1 for _ in range(N+1)]

def root(i):
  while ids[i] != i: i = ids[i]
  return i

def connected(a, b):
  return root(a) == root(b)

def union(a, b):
  id1, id2 = root(a), root(b)
  if id1 == id2:
    return
  
  if size[id1] < size[id2]:
    ids[id1] = id2
    size[id2] += size[id1]
  else:
    ids[id2] = id1
    size[id1] += size[id2]


for v in range(N):
  x = list(map(int, input().split()))
  for i, d in enumerate(x):
    if d == 1:
      union(v+1, i+1)
  
ans = list(map(int, input().split()))

for i in range(len(ans)-1):
  s = ans[i]; e = ans[i+1]
  if not connected(s, e):
    print('NO')
    exit(0)

print('YES')