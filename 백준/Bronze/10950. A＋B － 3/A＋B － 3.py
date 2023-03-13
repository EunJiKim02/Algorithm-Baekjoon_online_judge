n = int(input())
list1 = []
for _ in range(n):
    a, b = map(int, input().split())
    list1.append(a+b)

for i in range(n):
    print(list1[i])
