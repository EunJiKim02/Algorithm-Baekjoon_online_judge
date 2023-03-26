arr = list(map(int, input().split()))

arr.sort()

s = arr[0] + arr[1]
x = arr[2]
while(True):
    if(s > x):
        print(s + x)
        break
    x -= 1

