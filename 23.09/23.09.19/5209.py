T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    min_expense = 99 * N * N
    made = [0] * N


    def factory(num, expense):
        global min_expense
        if expense >= min_expense:
            return
        elif num == N:
            min_expense = min(min_expense, expense)
            return
        else:
            for product in range(N):
                if made[product] == 0:
                    made[product] = 1
                    factory(num + 1, expense + V[product][num])
                    made[product] = 0


    factory(0, 0)
    print(f"#{tc} {min_expense}")
