import sys
sys.setrecursionlimit(10 ** 6)

# 0, 1, 2, 3 -> xs = 0 , n = 4

def cutpapar(cnt, paper, x, y, n):
    out = False
    check = paper[x][y]
    for i in range(n):
        for j in range(n):
            if(paper[x + i][y + j] != check):
                cnt = cutpapar(cnt, paper, x , y, n//2)
                cnt = cutpapar(cnt, paper, x , y + n//2, n//2)
                cnt = cutpapar(cnt, paper, x + n//2 , y , n//2)
                cnt = cutpapar(cnt, paper, x + n//2 , y + n//2, n//2)
                out = True
                break
        if out:
            break
                
    if(i == n-1 and j == n-1 and not out):
        if(check == 0):
            return (cnt[0] + 1, cnt[1])
        else:
            return (cnt[0], cnt[1] + 1)
    else:
        return (cnt[0], cnt[1])


n = int(input())

count = [0, 0]
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

count = cutpapar(count, paper, 0, 0, n)
print(count[0])
print(count[1])
