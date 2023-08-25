bingo_list = []
answer_list = []

for n in range(5):
    bingo_list.append(list(map(int, input().split())))

for m in range(5):
    answer_list.append(list(map(int, input().split())))

bingo_line = 0


def is_three_bingo(check_list):
    global bingo_line
    for i in range(5):
        bingo = 0
        bingo = sum(check_list[i])
        if bingo == 0:
            bingo_line += 1
    for j in range(5):
        bingo = 0
        for column_number in range(5):
            bingo += check_list[column_number][j]
        if bingo == 0:
            bingo_line += 1
    if check_list[2][2] + check_list[0][4] + check_list[1][3] + check_list[4][0] + check_list[3][1] == 0:
        bingo_line += 1
    if check_list[2][2] + check_list[0][0] + check_list[1][1] + check_list[3][3] + check_list[4][4] == 0:
        bingo_line += 1

    if bingo_line == 3:
        return True
    else:
        bingo_line = 0
        return False


bingo_dict = dict()

for q in range(5):
    for p in range(5):
        bingo_dict.update({bingo_list[q][p]: (q, p)})

break_now = False

for y in range(5):
    for x in range(5):
        bingo_y, bingo_x = bingo_dict[answer_list[y][x]]
        formal_number = bingo_list[bingo_y][bingo_x]
        bingo_list[bingo_y][bingo_x] = 0
        if is_three_bingo(bingo_list) is True:
            the_number = formal_number
            break_now = True
            break
    if break_now:
        break

print(the_number)
