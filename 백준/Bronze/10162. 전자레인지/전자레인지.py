time = [300, 60, 10]
n = int(input())
ans = []
for t in time:
    ans.append(n // t)
    n = n % t

if n != 0 :
    print(-1)
else:
    print(ans[0], ans[1], ans[2])
