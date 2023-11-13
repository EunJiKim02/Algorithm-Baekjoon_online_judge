m = [500, 100, 50, 10, 5, 1]

n = int(input())
n = 1000 - n
count = 0
for mm in m:
    count += (n // mm)
    n %= mm

print(count)