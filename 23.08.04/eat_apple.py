T = int(input())


def change_dir(input_dir, y, x):
    if input_dir == 0:
        return y, x
    if input_dir == 2:
        return -y, -x
    if input_dir == 1:
        return x, y
    if input_dir == 3:
        return x, -y


for tc in range(1, T + 1):
    N = int(input())
    field = []

    for _ in range(N):
        field.extend(map(int, input().split()))

    M = max(field)
    start_index = 0
    turn_right = 0
    direction = 0  # right : 0, down : 1, left : 2, up : 3

    for m in range(1, M + 1):
        end_index = field.index(m)
        start_x = start_index % N
        start_y = start_index // N
        end_x = end_index % N
        end_y = end_index // N

        if change_dir(direction, end_y - start_y, end_x - start_x)[0] > 0 and \
                change_dir(direction, end_y - start_y, end_x - start_x)[1] > 0:
            turn_right += 1
            direction = (direction + 1) % 4
            print(change_dir(direction, end_y - start_y, end_x - start_x)[0])
            print(change_dir(direction, end_y - start_y, end_x - start_x)[1])
            print(turn_right)
            print(direction)
        elif change_dir(direction, end_y - start_y, end_x - start_x)[0] > 0 and \
                change_dir(direction, end_y - start_y, end_x - start_x)[1] < 0:
            turn_right += 2
            direction = (direction + 2) % 4
            print(change_dir(direction, end_y - start_y, end_x - start_x)[0])
            print(change_dir(direction, end_y - start_y, end_x - start_x)[1])
            print(turn_right)
            print(direction)
        elif change_dir(direction, end_y - start_y, end_x - start_x)[0] < 0 and \
                change_dir(direction, end_y - start_y, end_x - start_x)[1] < 0:
            turn_right += 3
            direction = (direction + 3) % 4
            print(change_dir(direction, end_y - start_y, end_x - start_x)[0])
            print(change_dir(direction, end_y - start_y, end_x - start_x)[1])
            print(turn_right)
            print(direction)
        elif change_dir(direction, end_y - start_y, end_x - start_x)[0] < 0 and \
                change_dir(direction, end_y - start_y, end_x - start_x)[1] > 0:
            turn_right += 3
            direction = (direction + 3) % 4
            print(change_dir(direction, end_y - start_y, end_x - start_x)[0])
            print(change_dir(direction, end_y - start_y, end_x - start_x)[1])
            print(turn_right)
            print(direction)

        start_index = end_index

    print(f"#{tc} {turn_right}")
