import sys
arr = list(map(int, input().split()))
lena = len(arr) - 1
n = arr[-1]
sarr = sum(arr[:-1])
count = 0

while sarr/lena <n:
  count+=1
  sarr +=1

print(count)
