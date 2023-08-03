direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
K = int(input())
field = []

for n in range(N):
    field.append(list(input()))

for y in range(N):
    for x in range(M):
        if field[y][x] == "@":
            for y_dir, x_dir in direction:
                for k in range(1, K + 1):
                    if 0 <= y + k * y_dir < N and 0 <= x + k * x_dir < M:
                        if field[y + k * y_dir][x + k * x_dir] == "#":
                            break
                        if field[y + k * y_dir][x + k * x_dir] == "_":
                            field[y + k * y_dir][x + k * x_dir] = "%"

            field[y][x] = "%"

for n in range(N):
    for m in range(M):
        print(field[n][m], end="")
    print()
