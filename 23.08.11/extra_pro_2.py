N = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]
path_list = list()
path = list()
now = 0
visited = [0] * N

while True:
    if now not in path:
        path.append(now)
        visited[now] = 1

    for to in range(N):
        if adj_matrix[now][to] and not visited[to]:
            now = to
            break
    else:
        if path:
            if len(path) == 3:
                print(*path)
                path.pop()
                visited[path[-1]] = 0
                now = path[-1]
            else:
                path.pop()
                if path:
                    visited[path[-1]] = 0
                    now = path[-1]
                else:
                    break
        else:
            break
