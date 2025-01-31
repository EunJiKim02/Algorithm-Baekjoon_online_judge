
def check(lan, length, mid):
    if length == 0:
        return True
    cnt = 0
    sinx = 0
    for i in range(1, len(lan)):
        dis = lan[i] - lan[sinx]
        if dis >= mid:
            cnt += 1
            sinx = i
    if cnt >= length:
        return True
    else:
        return False


N, C = map(int, input().split())

lan = list()
for _ in range(N):
    l = int(input())
    lan.append(l)

lan.sort()


start = 0
end = lan[-1]
answer = 0

while(start <= end):
    mid = (start + end) // 2
    if check( lan, C-1 ,mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1


print(answer)