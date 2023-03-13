
n = int(input())
arr = []

for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))
arr.sort()

count = 0
endtime = 0

for n in arr:
    start = n[0]
    end = n[1]
    if((start == end) and (start >= endtime)):
        count += 1
        endtime = end
        continue
    elif(endtime > end):
        endtime = end
        continue
    elif(endtime <= start):
        count += 1
        endtime = end
print(count)