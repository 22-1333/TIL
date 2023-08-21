T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    answer_sheet_list = [list(map(int, input().split())) for _ in range(N)]
    min_score = None
    max_score = None

    for answer_sheet in answer_sheet_list:
        total_score = 0
        score = 0
        for idx in range(len(answer_sheet)):
            if answer[idx] == answer_sheet[idx]:
                score += 1
                total_score += score
            else:
                score = 0
        try:
            min_score = min(min_score, total_score)
            max_score = max(max_score, total_score)
        except TypeError:
            min_score = total_score
            max_score = total_score

    print(f"#{tc} {max_score - min_score}")
