n = int(input())

for _ in range(n):
    k, s = input().split()
    k = int(k)
    
    for sx in s:
        print(sx * k, end='')
    print()