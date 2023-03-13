sen = input()
operator = []
operand = []

n = 0
for i in sen:
  match i:
    case '+':
      operator.append('+')
      operand.append(n)
      n = 0
    case '-':
      operator.append('-')
      operand.append(n)
      n = 0
    case _:
      n = (n * 10) + int(i)

operand.append(n)


check = True # T면 plus, F면 minus
result = operand[0]
for i, v in enumerate(operator, start=1):
  if(v == '-'):
    check = False
  if check:
    result += operand[i]
  else:
    result -= operand[i]

print(result)