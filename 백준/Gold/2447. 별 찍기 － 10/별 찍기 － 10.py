import sys
sys.setrecursionlimit(10**6)

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]


def recur(N, i, j):
    if N == 1:
        arr[i][j] = 1
        return
    NextN = N // 3
    recur(NextN, i, j)
    recur(NextN, i, j + NextN)
    recur(NextN, i, j + 2 * NextN)

    recur(NextN, i + NextN, j)
    recur(NextN, i + NextN, j + 2 * NextN)

    recur(NextN, i + 2 * NextN, j)
    recur(NextN, i + 2 * NextN, j + NextN)
    recur(NextN, i + 2 * NextN, j + 2 * NextN)

recur(N, 0, 0)

for l in arr:
    for x in l:
        if x == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print()