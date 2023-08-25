T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    max_fly_kill = 0

    for y in range(N):
        for x in range(N):
            fly_kill = fly_list[y][x]
            dir_1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dy, dx in dir_1:
                for m in range(1, M):
                    if 0 <= y + m * dy < N and 0 <= x + m * dx < N:
                        fly_kill += fly_list[y + m * dy][x + m * dx]

            max_fly_kill = max(max_fly_kill, fly_kill)

            fly_kill = fly_list[y][x]
            dir_2 = [(1, 1), (-1, -1), (-1, 1), (1, -1)]

            for dy, dx in dir_2:
                for m in range(1, M):
                    if 0 <= y + m * dy < N and 0 <= x + m * dx < N:
                        fly_kill += fly_list[y + m * dy][x + m * dx]

            max_fly_kill = max(max_fly_kill, fly_kill)

    print(f"#{tc} {max_fly_kill}")
