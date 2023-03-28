n, m= map(int, input().split())
answer = []

def findans(k):
    if len(answer) == m:
        for x in answer:
            print(x, end= ' ')
        print()
        return
    for i in range(k, n+1):
        answer.append(i)
        findans(i)
        answer.pop()
        
findans(1)