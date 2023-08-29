T = int(input())
for tc in range(1, T + 1):
    N, W = map(int, input().split())
    score_list = list(map(int, input().split()))
    max_score = sum(score_list[:W])
    max_idx_start = 0
    max_idx_end = W - 1

    for idx in range(N - W + 1):
        score = sum(score_list[idx:idx + W])
        if score > max_score:
            max_score = score
            max_idx_start = idx
            max_idx_end = idx + W - 1

    print(f"#{tc}", max_idx_start, max_idx_end, max_score)
