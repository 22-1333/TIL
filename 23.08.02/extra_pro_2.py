import copy

map_arr = [["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"]]

y_size, x_size = map(int, input().split())
y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())


def bomb(y, x):

    direction = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

    for y_move, x_move in direction:
        if y + y_move < y_size and x + x_move < x_size:
            map_arr[y + y_move][x + x_move] = "#"


bomb(y1, x1)
bomb(y2, x2)

for i in map_arr:
    for j in i:
        print(j, end=" ")
    print()
