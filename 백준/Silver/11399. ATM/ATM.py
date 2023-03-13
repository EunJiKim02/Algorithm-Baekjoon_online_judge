n = int(input())
p = list(map(int, input().split()))
p.sort()
p.reverse()
result = 0
cnt = 1
for i in p:
  result += (i * cnt)
  cnt += 1

print(result) 