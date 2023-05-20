x = input()
y = input()

lcs = [[[0, 0] for _ in range(len(y) + 1)] for _ in range(len(x)+1)]

CROSS = 0
UP = 1
LEFT = 2

for j in range(1, len(x) + 1):
    for i in range(1, len(y) + 1):
        if x[j-1] == y[i-1]:
            lcs[j][i][0] = lcs[j-1][i-1][0] + 1
            lcs[j][i][1] = CROSS
        elif(lcs[j-1][i][0] < lcs[j][i-1][0]):
            lcs[j][i][0] = lcs[j][i-1][0]
            lcs[j][i][1] = UP
        else:
            lcs[j][i][0] = lcs[j-1][i][0]
            lcs[j][i][1] = LEFT


print(lcs[j][i][0])

result = []

while(1):
    if(lcs[j][i][0] == 0):
        break
    if lcs[j][i][1] == CROSS:
        result.append(x[j-1])
        j -= 1
        i -= 1
    elif lcs[j][i][1] == LEFT:
        j -= 1
    else:
        i -= 1

result.reverse()
for x in result:
    print(x, end='')
