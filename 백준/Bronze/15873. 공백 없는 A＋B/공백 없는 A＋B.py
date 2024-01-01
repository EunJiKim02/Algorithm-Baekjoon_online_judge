a = int(input())
if a % 10 == 0:
    print(a // 100 + a %100)
else:
    print(a // 10 + a % 10)