N,M = map(int,input().split())
A  = []
B = []
for i in range(N):
    A.append(list(map(int,input().split())))

for i in range(N):
    B.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]

for x in A:
    for y in x:
        print(y,end=' ')
    print()
        
