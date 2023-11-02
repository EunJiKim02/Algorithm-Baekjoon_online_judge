import sys
input = sys.stdin.readline
N = int(input())
pointX = []
pointY = []
for _ in range(N):
    x, y = map(int, input().split())
    pointX.append(x)
    pointY.append(y)

xmin = min(pointX)
xmax = max(pointX)
ymin = min(pointY)
ymax = max(pointY)

print((xmax-xmin) * (ymax-ymin))