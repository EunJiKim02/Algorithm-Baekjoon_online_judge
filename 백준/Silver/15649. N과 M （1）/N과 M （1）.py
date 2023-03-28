n, m = map(int, input().split())
visited = []

def dfs():
    if len(visited) == m:
        for x in visited:
            print(x, end=' ')
        print()
        return
    for i in range(1, n+1):
        if i not in visited:
            visited.append(i)
            dfs()
            visited.pop()

dfs()