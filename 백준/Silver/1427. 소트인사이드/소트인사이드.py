N = input()

k = list(map(int, N))

k.sort()
k.reverse()
for x in k:
    print(x, end='')