T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    base = [n for n in range(N)]
    min_total = 10 * N
    cnt = 0


    def f(i, n, t):
        global min_total
        global cnt
        if i == n:
            total = 0
            for idx in range(N):
                if total >= min_total:
                    break
                else:
                    total += arr[base[idx]][idx]
            min_total = min(min_total, total)
        else:
            for j in range(i, n):
                base[i], base[j] = base[j], base[i]
                if t < min_total:
                    f(i + 1, n, t + arr[base[i]][i])
                base[i], base[j] = base[j], base[i]


    f(0, N, 0)
    print(f"#{tc} {min_total}")
