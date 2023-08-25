N = int(input())
field = list()

for _ in range(N):
    field.append(list(map(int, input().split())))

direction = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

K = int(input())

max_kill = 0

for y in range(N):
    for x in range(N):
        kill = 0

        for k in range(1, K + 1):
            for y_dir, x_dir in direction:
                if 0 <= y + k * y_dir < 5 and 0 <= x + k * x_dir < 5:
                    kill += field[y + y_dir][x + x_dir]

        max_kill = max(max_kill, kill)

print(max_kill)
