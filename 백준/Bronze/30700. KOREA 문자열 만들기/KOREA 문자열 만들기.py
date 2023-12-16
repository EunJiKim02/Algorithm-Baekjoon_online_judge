s = input()

k = ['K', 'O', 'R', 'E', 'A']
cnt = 0
for i in s:
    if i == k[cnt%5]:
        cnt += 1
print(cnt)