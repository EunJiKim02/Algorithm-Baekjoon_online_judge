import sys
k = int(input())
for _ in range(k):
    n = input()
    length = len(n)
    if (length >=6) and (length <=9):
        print('yes')
    else:
        print('no')