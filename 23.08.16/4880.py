T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    game_group = list(map(int, input().split()))
    card_list = [0]
    card_list.extend(game_group)
    group_member = [n for n in range(1, N + 1)]


    def game_winner(player_1, player_2):
        if card_list[player_1] == 1:
            if card_list[player_2] == 1:
                return player_1
            elif card_list[player_2] == 2:
                return player_2
            elif card_list[player_2] == 3:
                return player_1
        elif card_list[player_1] == 2:
            if card_list[player_2] == 1:
                return player_1
            elif card_list[player_2] == 2:
                return player_1
            elif card_list[player_2] == 3:
                return player_2
        elif card_list[player_1] == 3:
            if card_list[player_2] == 1:
                return player_2
            elif card_list[player_2] == 2:
                return player_1
            elif card_list[player_2] == 3:
                return player_1


    def group_winner(group):
        if len(group) == 1:
            return group[0]
        elif len(group) == 2:
            return game_winner(group[0], group[1])
        else:
            return game_winner(group_winner(group[:(len(group) - 1) // 2 + 1]), group_winner(group[(len(group) - 1) // 2 + 1:]))


    print(f"#{tc} {group_winner(group_member)}")
