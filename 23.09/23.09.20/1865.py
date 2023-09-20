T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    worked = [0] * N
    max_p = 0


    def work(n, p):
        global max_p, N

        if n == N - 1:
            max_p = max(max_p, p * P[worked.index(0)][N - 1] * 0.01)
            print(worked)
            print(p * P[worked.index(0)][N - 1] * 0.01)
            return
        else:
            for staff in range(N):
                if not worked[staff]:
                    if p * P[staff][n] * 0.01 <= max_p:
                        # print("wrong", p * P[staff][n] * 0.01)
                        continue

                    worked[staff] = n + 1
                    work(n + 1, p * P[staff][n] * 0.01)
                    worked[staff] = 0


    work(0, 100)
    print(f"#{tc} {round(max_p, 6)}")
