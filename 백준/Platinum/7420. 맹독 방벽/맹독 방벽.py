import sys
import math

input = sys.stdin.readline

def myround(n):
  if (n - int(n)) >= 0.5:
    return int(n) + 1
  else:
    return int(n)

def ccw(i, j, k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0:
        return True
    else:
        return False 

def ConvexHull(point, N): 
    # 시작점 찾기 ( y 값이 가장 작은 값 )
    minindex = 0
    for i in range(1, N): # ~N
      if point[minindex][1] > point[i][1]:
        minindex = i
      elif  (point[minindex][1] == point[i][1]) and(point[minindex][0] < point[i][0]):
        minindex = i
    
    startp = point[minindex]

    # 시작점 p를 기준으로 각도 구해서 정렬하기 
    bangle = [] # (x, y, angle)
    for i in range(N): # ~N
      a = math.atan2(point[i][1] - startp[1], point[i][0] - startp[0])
      bangle.append((point[i][0], point[i][1], a))

    angle = sorted(bangle, key=lambda x : (x[2], x[1], ~x[0]))

    # 탐색하면서 convexhull에 들어가는 값 찾기
    stack = []
    stack.append((angle[0][0], angle[0][1]))
    stack.append((angle[1][0], angle[1][1]))

    for i in range(2, N):
        while (len(stack) > 2) and not ccw( stack[-2], stack[-1], angle[i]):
            stack.pop()
      
        stack.append((angle[i][0], angle[i][1]))

    return stack

# 유클리드 거리 구하기
def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def curvedistance(a, b, c, k):
    A = round(distance(a, b),10)
    B = round(distance(b, c), 10)
    C = round(distance(c, a), 10)

    costheta = round((A ** 2 + B ** 2 - C ** 2) / (2 * A * B), 10)
    #print(a, b, c)
    #print(A, B, C, costheta)
    ang = math.acos(costheta)
    #print(ang)
    return (k) * (math.pi - ang)

def getlength(convex, L):
    convex.append(convex[0])
    N = len(convex)
    #print(convex, N)
    linelength = 0
    curvelength = 0
    for i in range(N-1): # ~N
        linelength += distance(convex[i], convex[i+1])
    #print(linelength)
    for i in range(N-2): # ~N
      #print(i)
      curvelength += curvedistance(convex[i], convex[i+1], convex[i+2], L)
    curvelength += curvedistance(convex[-2], convex[-1], convex[1], L)
    return myround(linelength + curvelength)


N, L = map(int, input().split())
#N = int(input())
point = [[0, 0] for _ in range(N)]

# init
for i in range(N):
    a, b = map(int, input().split())
    point[i][0], point[i][1] = a, b

convexresult = ConvexHull(point, N)
#print(convexresult)
print(getlength(convexresult, L))
