answer = [0 for _ in range(9)] 
for i in range(9):
    answer[i] = int(input())
    
MAX = max(answer)
print(MAX)
print(answer.index(MAX) + 1)