n, m = map(int, input().split())

number = list(map(int, input().split()))
number.sort()

answer = []
def findans():
    if len(answer) == m:
        for x in answer:
            print(x, end = ' ')
        print()
        return
    for k in number:
        if k not in answer:
            answer.append(k)
            findans()
            answer.pop()
            
            
findans()