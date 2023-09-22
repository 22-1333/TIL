T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    times = [0] * N


    def go_x():
        global N, X

        for n in range(N):
            index = n
            shortest_way = [((N - 1) * 10000, 0)] * N
            shortest_way[n] = (0, 0)

            level = 0
            while level < N:
                for x, y, c in roads:
                    if x == n + 1 and shortest_way[x - 1][0] + c < shortest_way[y - 1][0]:
                        shortest_way[y - 1] = (shortest_way[x - 1][0] + c, shortest_way[y - 1][1])

                next_n_way = (N - 1) * 10000
                next_n = n

                for n1 in range(N):
                    if shortest_way[n1][1] == 0 and shortest_way[n1][0] < next_n_way:
                        next_n = n1
                        break
                shortest_way[next_n] = (shortest_way[next_n][0], 1)
                n = next_n
                level += 1
                if n == X - 1:
                    break

            times[index] += shortest_way[X - 1][0]


    def x_go():
        global N, X
        shortest_way = [((N - 1) * 10000, 0)] * N
        shortest_way[X - 1] = (0, 1)
        n = X - 1

        level = 0
        while level < N:
            for x, y, c in roads:
                if x == n + 1 and shortest_way[x - 1][0] + c < shortest_way[y - 1][0]:
                    shortest_way[y - 1] = (shortest_way[x - 1][0] + c, shortest_way[y - 1][1])

            next_n_way = (N - 1) * 10000
            next_n = n

            for n1 in range(N):
                if shortest_way[n1][1] == 0 and shortest_way[n1][0] < next_n_way:
                    next_n = n1
                    break
            shortest_way[next_n] = (shortest_way[next_n][0], 1)
            n = next_n
            level += 1

        for index in range(N):
            times[index] += shortest_way[index][0]


    go_x()
    x_go()

    print(f"#{tc} {max(times)}")
