import sys
input = sys.stdin.readline

N = 9

arr = []
maxin = [0,0]
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if arr[i][j] > arr[maxin[0]][maxin[1]]:
            maxin[0], maxin[1] = i, j
            
print(arr[maxin[0]][maxin[1]])
print(maxin[0]+1, maxin[1]+1)