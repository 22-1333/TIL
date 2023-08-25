T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for idx in range(N - M + 1):
        m_sum = 0
        for sum_idx in range(M):
            m_sum += arr[idx + sum_idx]
        if idx == 0:
            min_sum, max_sum = m_sum, m_sum
        if m_sum > max_sum:
            max_sum = m_sum
        if m_sum < min_sum:
            min_sum = m_sum
    print(f"#{tc} {max_sum - min_sum}")
