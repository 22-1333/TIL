gomoku_board = []

for _ in range(19):
    gomoku_board.append(list(map(int, input().split())))


def how_many_in_a_row(y, x, color, dir_y=0, dir_x=0):
    direction = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

    for to_y, to_x in direction:
        if 0 <= y + to_y < 19 and 0 <= x + to_x < 19:
            if gomoku_board[y + to_y][x + to_x] == color:
                if color != 0:
                    return 1 + how_many_in_a_row(y + to_y, x + to_x, color, dir_y=to_y, dir_x=to_x)
                if color == 0:
                    return 0
        else:
            return 0


how_many_in_a_row(2, 1, gomoku_board[2][1])

# for j in range(19):
#     for i in range(19):
#         if how_many_in_a_row(j, i, gomoku_board[j][i]) >= 5:
#             print(j, i, how_many_in_a_row(j, i, gomoku_board[j][i]))
