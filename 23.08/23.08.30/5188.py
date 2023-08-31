T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    movings = list()
    for _ in range(N):
        movings.append((0, 1))
        movings.append((1, 0))
    p = [0] * (2 * (N - 1))
    used = [0] * (2 * (N - 1))
    min_score = 10 * (2 * N - 1)
    p_list = list()


    def f(i, k):
        global min_score
        if i == k:
            y, x, score = 0, 0, board[0][0]
            for dy, dx in p:
                y, x = y + dy, x + dx
                score += board[y][x]
            min_score = min(min_score, score)
            return
        else:
            for j in range(2 * (N - 1)):
                if used[j] == 0:
                    p[i] = movings[j]
                    used[j] = 1
                    f(i + 1, k)
                    used[j] = 0


    f(0, 2 * (N - 1))
    print(f"#{tc} {min_score}")
