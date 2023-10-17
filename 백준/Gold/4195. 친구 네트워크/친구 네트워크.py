import sys
input = sys.stdin.readline

ids = []
size = []

def root(i):
  while ids[i]!=i: i = ids[i]
  return i

def connected(p, q):
  return root(p) == root(q)

def union(p, q):
  id1, id2 = root(p), root(q)
  if id1 == id2: return
  if size[id1] <= size[id2]:
    ids[id1] = id2
    size[id2] += size[id1]
  else:
    ids[id2] = id1
    size[id1] += size[id2]



N = int(input())

for _ in range(N):
  F = int(input())
  i = 0
  humaninfo = dict()

  for _ in range(F):
    a, b = input().split()
    if a not in humaninfo:
      humaninfo[a] = i
      size.append(1)
      ids.append(i)
      i+=1
    if b not in humaninfo:
      humaninfo[b] = i
      size.append(1)
      ids.append(i)
      i+=1
    ai, bi = humaninfo[a], humaninfo[b]
    union(ai, bi)
    print(size[root(ai)])


    


  size.clear()
  ids.clear()
