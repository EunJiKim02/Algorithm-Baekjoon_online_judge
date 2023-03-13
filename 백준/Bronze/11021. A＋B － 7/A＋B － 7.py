n = int(input())
list1 = []
for _ in range(n):
    a, b = map(int, input().split())
    list1.append(a+b)

for i in range(n):
    print(f"Case #{i+1}: {list1[i]}")

