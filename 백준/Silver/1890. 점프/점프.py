import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

result = [[0 for _ in range(N)]for _ in range(N)]
result[0][0] = 1


for i in range(N+1):
    for x in range(i):
        Xi = x
        Yj = i - x - 1

        k = arr[Xi][Yj]
        if k + Xi < N:
            result[Xi + k][Yj] += result[Xi][Yj]
        if k + Yj < N:
            result[Xi][Yj + k] += result[Xi][Yj]


        
for i in range(N-1, -1, -1): # 2 1 0
    for x in range(i): # 0 1 2 / 0 1 / 0
        Xi = x+1 + (N-1-i)
        Yj = N-x-1

        k = arr[Xi][Yj]
        if k == 0:
            break
        if k + Xi < N:
            result[Xi + k][Yj] += result[Xi][Yj]
        if k + Yj < N:
            result[Xi][Yj + k] += result[Xi][Yj]
    
print(result[N-1][N-1])