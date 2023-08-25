map_arr = [[3, 3, 5, 3, 1], [2, 2, 4, 2, 6], [4, 9, 2, 3, 4], [1, 1, 1, 1, 1], [3, 3, 5, 9, 2]]
N = 5


def sum_map(y, x):
    left_top = map_arr[y + 1][x + 1]
    right_top = map_arr[y + 1][x - 1]
    left_bottom = map_arr[y - 1][x + 1]
    right_bottom = map_arr[y - 1][x - 1]

    return left_top + right_top + left_bottom + right_bottom


max_sum = 0
max_y = 1
max_x = 1

for i in range(1, N - 1):
    for j in range(1, N - 1):
        if sum_map(j, i) >= max_sum:
            max_sum = sum_map(j, i)
            max_y = j
            max_x = i

print(max_y, max_x)
