n = int(input())
number = [0 for _ in range(n)]
for i in range(n):
    number[i] = int(input())

for i in range(n -1):
    for j in range(i,n):
        if(number[i] > number[j]):
            number[i], number[j] = number[j], number[i]


for x in number:
    print(x)        