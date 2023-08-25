T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_area = 0
    counting = 0

    for j in range(N):
        for i in range(N):
            for y in range(j, N):
                for x in range(i, N):
                    if board[j][i] == board[y][x]:
                        area = (y - j + 1) * (x - i + 1)
                        if max_area < area:
                            max_area = area
                            counting = 1
                        elif max_area == area:
                            counting += 1

    print(f"#{tc} {counting}")
