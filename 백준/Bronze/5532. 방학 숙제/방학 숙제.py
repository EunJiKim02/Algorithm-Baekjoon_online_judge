def up(x):
    if int(x) < x:
        return int(x) + 1
    else:
        return int(x)

l = int(input())
a = float(input())
b = float(input())
c = int(input())
d = int(input())

k1 = up(a/c)
k2 = up(b/d)
k = max(k1, k2)
print(l - k)