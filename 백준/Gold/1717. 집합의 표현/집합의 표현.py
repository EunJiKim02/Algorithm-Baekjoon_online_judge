import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 

ids = [x for x in range(n+1)]
size = [1 for _ in range(n+1)]

def root(i):
  while i != ids[i]: i = ids[i]
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

for _ in range(m):
  fu, a, b = map(int, input().split())
  if fu == 0:
    union(a, b)

  else:
    if connected(a, b):
      print("YES")
    else:
      print("NO")

  