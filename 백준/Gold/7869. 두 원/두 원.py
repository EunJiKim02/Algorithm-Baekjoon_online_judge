import math

def distance(A, B):
  return math.sqrt((A[0] - B[0])**2 +(A[1] - B[1]) ** 2)

def getangle(a, b, c): # a와 b 사이의 각
  cosAngle = ( a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
  return math.acos(cosAngle)

A = [0, 0]
B = [0, 0]

A[0], A[1], r1, B[0], B[1], r2 = map(float, input().split())



if distance(A, B) > (r1 + r2): # 전혀 겹치지 않을 때
  result = 0
elif (distance(A,B) <= abs(r1-r2)): # 원이 내부에 속해있을 때
  r = min(r1, r2)
  result = r **2 * math.pi
else:
  theta1 = 2 * getangle(r1, distance(A,B), r2)
  theta2 = 2 * getangle(r2, distance(A,B), r1)

  # 부채꼴 넓이 구하기
  s1 = r1 * r1 * theta1 * 0.5
  s2 = r2 * r2 * theta2 * 0.5

  # 삼각형 넓이 구하기
  t1 = r1 * r1 * math.sin(theta1) * 0.5
  t2 = r2 * r2 * math.sin(theta2) * 0.5

  result = (s1 - t1) + (s2 - t2)

print(f"{round(result, 3):.3f}")