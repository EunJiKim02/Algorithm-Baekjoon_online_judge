
def check(lan, count, n):
    tmp = 0
    if n == 0:
        return True
    for l in lan:
        tmp += (l // n)
    if tmp >= count:
        return True
    else:
        return False

K, N = map(int, input().split())

lan = list()

for _ in range(K):
    l = int(input())
    lan.append(l)

start = 0
end = max(lan)
answer = 0

while(True):
    mid = (start + end) // 2
    if check(lan, N, mid):
        answer = mid
        start = mid+1
    else:
        end = mid-1
    if start > end:
        break

print(answer)


