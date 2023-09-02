import sys

ADD = 0; SUB = 1; MUL = 2; DIV = 3

# input
N = int(input())
operand = list(map(int, input().split()))
operator_num = list(map(int, input().split()))

operator = []
for i, k in enumerate(operator_num):
  for _ in range(k):
    operator.append([i, False])

def calculate(operator):
  result = operand[0]
  for i, k1 in enumerate(operator):
    k = k1[0]
    if k == ADD:
      result += operand[i+1]
    elif k == SUB:
      result -= operand[i+1]
    elif k == MUL:
      result *= operand[i+1]
    else:
      if result < 0:
        result = -1 * ((result * -1) // operand[i+1])
      else:
        result //= operand[i+1]

  return result

minres = sys.maxsize
maxres = sys.maxsize * -1

# permutation 을 기반으로 코드 작성
def bruteforce(cnt, pos, oper, res):
  if cnt == N-1:
    result = calculate(oper)
    global minres,maxres
    minres = min(result, minres)
    maxres = max(result, maxres)
    return result
  
  for i in range(len(operator)):
    if pos == i:
      continue
    if operator[i][1] == False:
      operator[i][1] = True
      oper.append(operator[i])
      res = bruteforce(cnt+1, i, oper, res)
      operator[i][1] = False
      oper.pop()

  return res

oper = []
bruteforce(0, -1, oper, 0)
print(maxres)
print(minres)