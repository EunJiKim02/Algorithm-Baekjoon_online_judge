
n = int(input())
stu = list(map(int, input().split()))
passnum = 1
temp = []
for i in range(n):
    s = stu[i]
    if s == passnum:
        passnum += 1
        while len(temp) > 0:
            top = temp[-1]
            if top == passnum:
                passnum += 1
                temp.pop()
            else:
                break
    else:
        if len(temp) == 0:
            temp.append(s)
        else:
            top = temp[-1]
            if s < top:
                temp.append(s)
            else:
                i -= 1
                break


if i == n-1:
    print("Nice")
else:
    print("Sad")