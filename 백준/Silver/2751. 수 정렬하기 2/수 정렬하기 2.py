import sys
input = sys.stdin.readline

def merge(a, aux, lo, mid, hi):
    for k in range(lo, hi+1):
        aux[k] = a[k]
    i, j = lo, mid+1
    for k in range(lo, hi+1):
        if i > mid: a[k], j = aux[j], j+1
        elif j > hi: a[k], i = aux[i], i+1
        elif aux[i] <= aux[j]: a[k], i = aux[i], i+1
        else: a[k], j = aux[j], j+1
        
def mergeSort(a):
    aux = [-1] * len(a)
    
    sz = 1
    while sz < len(a):
        for lo in range(0, len(a)-sz, sz*2):
            merge(a, aux, lo, lo+sz-1, min(lo+sz-1+sz, len(a)-1))
        sz *= 2
    
    return a

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
    
result = mergeSort(a)
for x in result:
    print(x)
