import sys

input = sys.stdin.readline

n, m = map(int, input().split())

isCycle = False
ans = 0

size = [1 for _ in range(n)]
ids = [x for x in range(n)]

def root(i):
  while i!= ids[i]: i = ids[i]
  return i

def connected(a, b):
  return root(a) == root(b)

def union(a, b):
  id1, id2 = root(a), root(b)
  if id1 == id2:
    global isCycle
    isCycle = True
    return
  if size[id1] < size[id2]:
    ids[id1] = id2
    size[id2] += size[id1]
  else:
    ids[id2] = id1
    size[id1] += size[id2]

first = True

for i in range(m):
  a, b = map(int, input().split())
  union(a, b)
  if isCycle and first:
    ans = i+1
    first = False

print(ans)
