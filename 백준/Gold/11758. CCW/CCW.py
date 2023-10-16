P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))


def ccw(a, b, c):
    return ((b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]))

result = ccw(P3, P2, P1)

if result > 0:
    print(-1)
elif result == 0:
    print(0)
else:
    print(1)
