T = int(input())
for tc in range(1, T + 1):
    S = list(input())
    card_dict = {"S": [], "D": [], "H": [], "C": []}
    insufficient_card_list = []

    for idx in range(len(S) // 3):
        if int(S[idx * 3 + 1]) * 10 + int(S[idx * 3 + 2]) in card_dict[S[idx * 3]]:
            print(f"#{tc} ERROR")
            break
        else:
            card_dict[S[idx * 3]].append(int(S[idx * 3 + 1]) * 10 + int(S[idx * 3 + 2]))
    else:
        for shape in card_dict:
            insufficient_card_list.append(13 - len(card_dict[shape]))

        print(f"#{tc}", *insufficient_card_list)
