import sys

INF = sys.maxsize
n = int(input())

# 자료구조 선언
stat = []
sumstat = [[0 for _ in range(n)] for _ in range(n)]

number = [i for i in range(n)]

stack = []
link_stack = []
STACK_MAX = n // 2
min_val = INF
start_team = 0
link_team = 0

# data input
for _ in range(n):
  stat.append(list(map(int, input().split())))

# data 전처리
for i in range(n):
  for j in range(i, n):
    sumstat[i][j] += (stat[i][j] + stat[j][i])
    sumstat[j][i] = sumstat[i][j]


def checkmin(check):
  n = len(check)
  start = 0
  link = 0
  for j in range(n):
    if check[j]:
      for i in range(j+1, n):
        if check[i]:
          start += sumstat[j][i]
    else:
      for i in range(j+1, n):
        if not check[i]:
          link += sumstat[j][i]
  return abs(start - link)




check = [False for _ in range(n)]

# cnt : 몇개가 true 처리 되어있는지
# pos : 시작점
# res : 결과값
def bruteforce(cnt, pos, res, check):
  if cnt == STACK_MAX:
    return checkmin(check)
  if pos == n:
    return INF
  check[pos] = True
  res = min(res, bruteforce(cnt+1, pos+1, res, check))
  check[pos] = False
  res = min(res, bruteforce(cnt, pos+1, res, check))
  return res

print(bruteforce(0, 0, INF, check))