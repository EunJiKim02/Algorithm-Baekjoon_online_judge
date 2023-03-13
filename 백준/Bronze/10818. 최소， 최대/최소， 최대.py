n = int(input())

list1 = list(input().split())
max = min = int(list1[0])

for i in range(len(list1)-1):
    if max <int(list1[i+1]):
        max = int(list1[i+1])
    elif min > int(list1[i+1]):
        min = int(list1[i+1])
print(min,max)