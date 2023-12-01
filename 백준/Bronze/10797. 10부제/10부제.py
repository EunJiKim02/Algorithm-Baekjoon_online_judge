n = int(input())
arr = map(int, input().split())
count = 0
for x in arr:
    if x == n:
        count += 1
print(count)