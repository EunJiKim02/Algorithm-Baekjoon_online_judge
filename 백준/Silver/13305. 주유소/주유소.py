n = int(input())

roadlength = list(map(int, input().split()))
gas = list(map(int, input().split()))

minvalue = gas[0]
money = 0
cnt = 1

for m in roadlength:
    money  += (minvalue * m)
    minvalue = min(gas[cnt], minvalue)
    cnt += 1


print(money)