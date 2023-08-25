T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    counting = 0

    for j in range(N):
        x = 0
        length = 0
        while x != N:
            if x == N - 1:
                if board[j][x] == 1:
                    if length + 1 == K:
                        counting += 1
                else:
                    if length == K:
                        counting += 1
                break
            elif board[j][x] == 0:
                if length == K:
                    counting += 1
                x += 1
                length = 0
            else:
                x += 1
                length += 1

    for i in range(N):
        y = 0
        length = 0
        while y != N:
            if y == N - 1:
                if board[y][i] == 1:
                    if length + 1 == K:
                        counting += 1
                else:
                    if length == K:
                        counting += 1
                break
            elif board[y][i] == 0:
                if length == K:
                    counting += 1
                y += 1
                length = 0
            else:
                y += 1
                length += 1

    print(f"#{tc} {counting}")
