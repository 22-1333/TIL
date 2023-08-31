T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    max_rooms = 0
    ans = (A[0][0], 0)
    total_visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not total_visited[i][j]:
                queue = [[i, j, 1]]
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                max_aij = 0
                while queue:
                    now_i, now_j, rooms = queue.pop(0)
                    total_visited[now_i][now_j] = 1
                    max_aij = max(max_aij, rooms)
                    for di, dj in directions:
                        if 0 <= now_i + di < N and 0 <= now_j + dj < N:
                            if A[now_i + di][now_j + dj] - A[now_i][now_j] == 1:
                                queue.append([now_i + di, now_j + dj, rooms + 1])

                if max_rooms < max_aij:
                    ans = (A[i][j], max_aij)
                    max_rooms = max_aij
                elif max_rooms == max_aij:
                    if ans[0] > A[i][j]:
                        ans = (A[i][j], max_aij)
    print(f"#{tc}", *ans)
