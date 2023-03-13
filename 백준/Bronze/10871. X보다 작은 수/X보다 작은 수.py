n, x = input().split()
list1 = list(input().split())
list2 = []
for i in range(int(n)):
    if int(list1[i]) < int(x):
        print(list1[i],end = " ")
