import sys
input = sys.stdin.readline
n = int(input())
name = []
count = 0
for _ in range(n):
    age, n = input().split()
    name.append([int(age),count, n])
    count += 1

name.sort()
for k in name:
    print(k[0], k[2])
