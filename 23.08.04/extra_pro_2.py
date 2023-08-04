import itertools

T = int(input())
game_board = []

for tc in range(1, T + 1):
    N = int(input())
    for _ in range(N):
        game_board.append(list(map(int, input().split())))

    total_square_count = 0

    # for number in number_set:
    #     same_number_index_list = list()
    #
    #     for idx in range(len(game_board)):
    #         if game_board[idx] == number:
    #             same_number_index_list.append(idx)
    #
    #     same_number_coordinate_list = list()
    #
    #     for same_number_index in same_number_index_list:
    #         same_number_coordinate_list.append([same_number_index % N, same_number_index // N])
    #
    #     pair_list = list(itertools.combinations(same_number_coordinate_list, 2))
    #     max_area = 0
    #     each_square_count = 0
    #
    #     for pair in pair_list:
    #         area = (abs(pair[0][0] - pair[1][0] + 1)) * (abs(pair[0][1] - pair[1][1] + 1))
    #         if area > max_area:
    #             max_area = area
    #             each_square_count = 1
    #             print(pair)
    #             print(each_square_count)
    #         elif area == max_area:
    #             each_square_count += 1
    #             print(pair)
    #             print(each_square_count)
    #
    #     total_square_count += each_square_count

    print(f"#{tc} {total_square_count}")
