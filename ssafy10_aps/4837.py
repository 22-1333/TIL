from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    case_count = 0

    all_cases = combinations(A, N)

    for case in all_cases:
        total_num = 0
        for num in case:
            total_num += num
        if total_num == K:
            case_count += 1

    print(f"#{tc} {case_count}")
