gomoku_board = []

for _ in range(19):
    gomoku_board.append(list(map(int, input().split())))

direction = [(0, 1), (-1, 1), (1, 0), (1, 1)]
winner = False
checked_list = list()


def how_many_in_a_row(formal_y, formal_x, to_y, to_x):
    if 0 <= formal_y + to_y < 19 and 0 <= formal_x + to_x < 19:
        if gomoku_board[formal_y + to_y][formal_x + to_x] == gomoku_board[formal_y][formal_x]:
            return 1 + how_many_in_a_row(formal_y + to_y, formal_x + to_x, to_y, to_x)
        else:
            return 0
    else:
        return 0


for y in range(len(gomoku_board)):
    for x in range(len(gomoku_board[y])):
        if gomoku_board[y][x] != 0:
            for dir_y, dir_x in direction:
                if 0 <= y + dir_y < 19 and 0 <= x + dir_x < 19:
                    if gomoku_board[y + dir_y][x + dir_x] == gomoku_board[y][x]:
                        if 0 <= y - dir_y < 19 and 0 <= x - dir_x < 19:
                            if gomoku_board[y - dir_y][x - dir_x] != gomoku_board[y][x]:
                                if 2 + how_many_in_a_row(y + dir_y, x + dir_x, dir_y, dir_x) == 5:
                                    winner = True
                                    print(gomoku_board[y][x])
                                    print(y + 1, x + 1)
                        else:
                            if 2 + how_many_in_a_row(y + dir_y, x + dir_x, dir_y, dir_x) == 5:
                                winner = True
                                print(gomoku_board[y][x])
                                print(y + 1, x + 1)

if winner is False:
    print(0)
