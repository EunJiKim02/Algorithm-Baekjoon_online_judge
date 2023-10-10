import math

def ccw(i, j, k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0:
        return True
    else:
        return False
    

def grahamScan(points):
    
    #시작점 p 찾기 ( y 값이 가장 작은 점 )
    pointlen = len(points)
    pindex = 0
    for i in range(1, pointlen):
        if points[i][1] < points[pindex][1]:
            pindex = i
        elif points[i][1] == points[pindex][1]:
            if points[i][0] > points[pindex][0]:
                pindex = i 
    
    p = points[pindex]

    # p와 다른 점 간 각도 계산
    # angle[n] = (anx, any, angle)
    # 각도 : (px, py)로 부터의 점 (ax, ay) 가 이루는 각도
    angle = []
    for i in range(pointlen):
        a = math.atan2(points[i][1] - p[1], points[i][0] - p[0])
        angle.append((points[i][0],points[i][1], a))

    # 각도로 정렬
    sortedpoint = sorted(angle, key=lambda p: (p[2], p[1], ~p[0]))
    # 새로운 점 반복해서 추가해보자
    result = []
    ix = sortedpoint[0][0]; iy = sortedpoint[0][1]
    jx = sortedpoint[1][0]; jy = sortedpoint[1][1]
    result.append((ix, iy))
    result.append((jx, jy))
    for n in range(2, pointlen):
        #블록 fail -> 점 삭제
        while (len(result)>=2) and (not ccw(result[-2], result[-1], (sortedpoint[n][0], sortedpoint[n][1]))):
            result.pop()
        #새로운 점 포함
        result.append((sortedpoint[n][0], sortedpoint[n][1]))
        
    return len(result)


n = int(input())
point = []
for _ in range(n):
    a, b = map(int,input().split())
    point.append((a, b))

print(grahamScan(point))