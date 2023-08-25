T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    profit = 0
    center = (N - 1) // 2

    for j in range(N):
        for i in range(abs(center - j), N - abs(center - j)):
            profit += farm[j][i]

    print(f"#{tc} {profit}")
