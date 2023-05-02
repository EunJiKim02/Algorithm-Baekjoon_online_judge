x = input()
y = input()

lcs = [[0 for _ in range(len(y) + 1)] for _ in range(len(x)+1)]


for j in range(1, len(x) + 1):
    for i in range(1, len(y) + 1):
        if x[j-1] == y[i-1]:
            lcs[j][i] = lcs[j-1][i-1] + 1
        else:
            lcs[j][i] = max(lcs[j-1][i], lcs[j][i-1])


print(lcs[j][i])