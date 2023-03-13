
count3 = 0
count5 = 0

num = int(input())

while(1):
    if(num % 5 == 0):
        count5 = num / 5
        print(int(count5+count3))
        break
    elif(num == 0):
        print(int(count3+count5))
        break
    elif(num < 0):
        print(-1)
        break
    num -= 3
    count3 +=1
