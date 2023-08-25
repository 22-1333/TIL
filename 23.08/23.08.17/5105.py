def start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "2":
                return i, j


def bfs(y, x):
    queue = list()
    queue.append((y, x))
    visited[y][x] = 1
    while queue:
        cy, cx = queue.pop(0)
        if arr[cy][cx] == "3":
            return visited[cy][cx] - 2
        for dy, dx in direction:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] != "1" and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    queue.append((ny, nx))
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    si, sj = start()
    print(f"#{tc} {bfs(si, sj)}")
