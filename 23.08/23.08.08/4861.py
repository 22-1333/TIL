T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    ans = str()

    for y in range(N):
        for x in range(N - M + 1):
            horizontal_line = str()

            for m in range(M):
                horizontal_line += board[y][x + m]

            reversed_horizontal_line = horizontal_line[::-1]

            if horizontal_line == reversed_horizontal_line:
                ans = horizontal_line
                break

        if ans != "":
            break

    for x_ in range(N):
        for y_ in range(N - M + 1):
            vertical_line = str()

            for m_ in range(M):
                vertical_line += board[y_ + m_][x_]

        reversed_vertical_line = vertical_line[::-1]

        if reversed_vertical_line == vertical_line:
            ans = vertical_line
            break

        if ans != "":
            break

    print(f"#{tc} {ans}")
