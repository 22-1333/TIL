T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    max_num = 0

    for i in range(N - 1):
        for j in range(i + 1, N):
            num = A[i] * A[j]
            while num > 0:
                num, Dk = num // 10, num % 10
                if Dk < num % 10:
                    break
            else:
                max_num = max(max_num, A[i] * A[j])

    if max_num == 0:
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {max_num}")
