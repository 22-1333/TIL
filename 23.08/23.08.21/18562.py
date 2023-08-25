T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    passenger_list = list(map(int, input().split()))
    max_feasibility = 0

    for first in range(N):
        for second in range(first + 2, N):
            if second < N:
                for third in range(second + 2, N):
                    if third < N:
                        for forth in range(third + 2, N):
                            if forth < N:
                                if 2 <= (first + N - forth):
                                    max_feasibility = max(max_feasibility, (passenger_list[first] + passenger_list[second]) ** 2 + (passenger_list[third] + passenger_list[forth]) ** 2)
                                    max_feasibility = max(max_feasibility, (passenger_list[first] + passenger_list[forth]) ** 2 + (passenger_list[second] + passenger_list[third]) ** 2)
                            else:
                                break
                    else:
                        break
            else:
                break

    print(f"#{tc} {max_feasibility}")
