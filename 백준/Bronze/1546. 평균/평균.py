N = int(input())
arr = list(map(int, input().split())) 
print(sum(x/max(arr) * 100 for x in arr) / N)
