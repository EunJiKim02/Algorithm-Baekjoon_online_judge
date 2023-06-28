n = int(input())

wire = []
length = [1 for _ in range(n+1)]

for _ in range(n):
    a, b = map(int, input().split())
    wire.append((a, b))

wire.sort()


for i, x in enumerate(wire):
    a = x[0]; b = x[1]
    for j in range(i):
        if b > wire[j][1]:
            length[i] = max(length[i], length[j] + 1)

m = max(length)

print(n - m)
        
