import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def tree_init(arr, tree, node, s, e):
    if s == e:
        tree[node] = arr[s-1]
        return tree[node]
    tree[node] = tree_init(arr, tree, node*2, s, (s+e) //2) + tree_init(arr, tree, node*2+1, (s+e)//2+1, e)
    return tree[node]

def changevalue(tree, newvalue, value_idx):
    s = value_idx
    update_value = newvalue - tree[value_idx] 
    while (s > 0):
        tree[s] += update_value
        s //= 2
    return tree

def partialsum(tree, node, b, c, s, e):
    
    if c < s: # b c s e
        return 0
    if b > e: # s e b c
        return 0
    if b <= s and e <= c: # b s e c 
        return tree[node]
    left = partialsum(tree, node*2, b, c, s, (s+e) // 2)
    right = partialsum(tree, node * 2 + 1, b, c, (s+e)//2+1, e)

    return left + right


N, M, K = map(int, input().split())

size = 0
while(pow(2, size) <= N):
    size += 1
leafstart = pow(2, size)

tree = [0 for _ in range(pow(2, size+1))]
arr = [0 for _ in range(pow(2, size))]


# input
for i in range(N):
    k = int(input())
    arr[i] = k


tree_init(arr, tree, 1, 1, pow(2, size))


for _ in range(K + M):
    a, b, c = map(int, input().split())

    if a == 1: # b번째 수를 c로 변경하기
        tree = changevalue(tree, c , b+leafstart-1)
    else: # b부터 c까지의 부분합 출력하기
        ans = partialsum(tree, 1, b, c, 1, pow(2, size))
        print(ans)