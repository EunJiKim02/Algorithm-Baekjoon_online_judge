
paper = []
result = [0, 0, 0]

def nofp(paper, x, y, n):
    c = paper[x][y]
    out = False
    i = 0
    j = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != c:
                k = n//3
                nofp(paper, x, y, n //3)
                nofp(paper, x + k, y, n //3)
                nofp(paper, x + 2 * k, y, n //3)
                nofp(paper, x, y + k, n //3)
                nofp(paper, x, y + 2 * k, n //3)
                nofp(paper, x + k, y + k, n //3)
                nofp(paper, x + k, y + 2 * k, n //3)
                nofp(paper, x + 2 * k, y + k, n //3)
                nofp(paper, x + 2 * k, y + 2 * k, n //3)
                out = True
                break
        if out:
            break
    if not out:
        if c == -1:
            result[0] += 1
        elif c == 0:
            result[1] += 1
        else:
            result[2] += 1

def main():
    n = int(input())
    for _ in range(n):
        paper.append(list(map(int, input().split())))

    nofp(paper, 0, 0, n)
    
    for x in result:
        print(x)
    

if __name__ == '__main__':
    main()