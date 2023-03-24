answer = []

def hanoi(start, assist, end, n):
    if n <= 0:
        return
    hanoi(start, end, assist, n-1)
    answer.append((start, end))
    hanoi(assist, start, end, n-1)


n = int(input())

hanoi(1, 2, 3, n)
print(len(answer))
for x in answer:
    print(x[0], x[1])