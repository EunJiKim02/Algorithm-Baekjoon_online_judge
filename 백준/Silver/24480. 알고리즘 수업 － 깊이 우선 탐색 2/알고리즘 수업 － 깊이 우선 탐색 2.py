import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
cnt = 0

def main():
    global count
    n, m, r = map(int,  input().split())
    visited = [0] * (n+1)
    graph = [[]for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for k in graph:
        k.sort(reverse=True)
    dfs(graph, r, visited)
    for i in visited[1:]:
        print(i)


def dfs(graph, v, visited):
    global cnt
    cnt += 1
    visited[v] = cnt
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)


main()



