n = int(input())
lista = []
listb = []
for _ in range(n):
    a, b = map(int, input().split())
    lista.append(a)
    listb.append(b)

for i in range(n):
    print(f"Case #{i+1}: {lista[i]} + {listb[i]} = {lista[i]+listb[i]}")

