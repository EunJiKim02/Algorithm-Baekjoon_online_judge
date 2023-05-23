import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
MAX = 5001

T = int(input())
MOD = 1000000007

k = [0 for _ in range(MAX+1)]
k[0] = 1
k[1] = 1

for i in range(2,MAX):
    for x in range(0, i):
        k[i] = (k[i]%MOD+ (k[x]*k[i-x-1])%MOD)%MOD

for _ in range(T):
    t = int(input())
    if(t %2 == 0):
        print(k[t//2])
    else:
        print(0) 
