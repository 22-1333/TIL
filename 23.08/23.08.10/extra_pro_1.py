lst = list(input())
N = len(lst)
adj = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]


def dfs(v):
    print(lst[v], end="")
    visited[v] = True

    for i in range(N):
        if adj[v][i] and not visited[i]:
            dfs(i)


dfs(0)
