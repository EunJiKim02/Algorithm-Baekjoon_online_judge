M,N = map(int, input().split())

num = [x for x in range(1, M+1)]

def brute(cnt, select):
  if cnt == N:
    for x in select:
      print(x, end=' ')
    print()
    return
  for x in num:
    select.append(x)
    brute(cnt+1, select)
    select.pop()
  return

sel = []
brute(0, sel)