from math import sqrt

n = int(input())

def sqrb(n):
    return int(sqrt(n))

for _ in range(n):
    a, b = map(int, input().split())
    length = b - a
    if(length == 1):
        print(1)
        continue
    if pow(sqrb(length), 2) == length:
         print(2 * sqrb(length)-1)
    elif ((length - pow(sqrb(length), 2)) <= ( pow(sqrb(length) + 1, 2) - pow(sqrb(length), 2))//2):
        print(2 * sqrb(length))
    else:
        print(2 * sqrb(length)+1)