# 4366

"""
T = int(input())
for tc in range(1, T + 1):
    A = input()
    B = list(input())

    N = len(A)
    M = len(B)

    binary = int(A, 2)
    bin_list = [0] * N
    for i in range(N):
        bin_list[i] = binary ^ (1 << i)

    for i in range(M):
        num1 = 0
        num2 = 0
        for j in range(M):
            if i != j:
                num1 = num1 * 3 + B[j]
                num2 = num2 * 3 + B[j]
            else:
                num1 = num1 * 3 + (B[j] + 1) % 3
                num2 = num2 * 3 + (B[j] + 1) % 3
        if num1 in bin_list:
            ans = num1
            break
        if num2 in bin_list:
            ans = num2
            break
    print(f"#{tc} {ans}")
"""

# 2817

"""
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    cnt = 0
    for i in range(1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += arr[j]
        if s == K:
            cnt += 1
    print(f"#{tc} {cnt}")
"""

"""
def f(i, n, s, k):
    global cnt
    if i == n:
        if s == k:
            cnt += 1
    else:
        f(i + 1, n, s + arr[i], k)
        f(i + 1, n, s, k)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    
    f(0, N, 0, K)
    print(f"#{tc} {cnt}")
"""

# 1861

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ones = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
                    ones[arr[i][j]] = 1

    max_cnt = 0
    max_start = 0
    c = 0
    for k in range(N * N, 0, -1):
        if ones[k]:
            c += 1
            if max_cnt < c:
                max_cnt = c
                max_start = k
            elif max_cnt == c:
                max_start = k
        else:
            c = 0
    print(f"#{tc} {max_start} {max_cnt}")
"""

# 10966
