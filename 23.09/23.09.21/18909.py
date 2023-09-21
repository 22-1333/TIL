T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    height_list = [list(map(int, input().split())) for _ in range(N)]
    min_fuel_list = [[1000 * 2 * N] * N for _ in range(N)]
    min_fuel_list[0][0] = 0

    queue = [(0, 0)]

    while queue:
        y, x = queue.pop(0)

        if y == N - 1 and x == N - 1:
            continue

        if y + 1 < N:
            if height_list[y][x] - height_list[y + 1][x] < 0:
                extra_f = - height_list[y][x] + height_list[y + 1][x] + 1
            else:
                extra_f = 1
            if min_fuel_list[y + 1][x] > min_fuel_list[y][x] + extra_f:
                min_fuel_list[y + 1][x] = min_fuel_list[y][x] + extra_f
                queue.append((y + 1, x))

        if x + 1 < N:
            if height_list[y][x] - height_list[y][x + 1] < 0:
                extra_f = - height_list[y][x] + height_list[y][x + 1] + 1
            else:
                extra_f = 1
            if min_fuel_list[y][x + 1] > min_fuel_list[y][x] + extra_f:
                min_fuel_list[y][x + 1] = min_fuel_list[y][x] + extra_f
                queue.append((y, x + 1))

        if y - 1 >= 0:
            if height_list[y][x] - height_list[y - 1][x] < 0:
                extra_f = - height_list[y][x] + height_list[y - 1][x] + 1
            else:
                extra_f = 1
            if min_fuel_list[y - 1][x] > min_fuel_list[y][x] + extra_f:
                min_fuel_list[y - 1][x] = min_fuel_list[y][x] + extra_f
                queue.append((y - 1, x))

        if x - 1 >= 0:
            if height_list[y][x] - height_list[y][x - 1] < 0:
                extra_f = - height_list[y][x] + height_list[y][x - 1] + 1
            else:
                extra_f = 1
            if min_fuel_list[y][x - 1] > min_fuel_list[y][x] + extra_f:
                min_fuel_list[y][x - 1] = min_fuel_list[y][x] + extra_f
                queue.append((y, x - 1))

    print(f"#{tc} {min_fuel_list[N - 1][N - 1]}")
