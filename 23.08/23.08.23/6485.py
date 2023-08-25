T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n_number_list = [tuple(map(int, input().split())) for _ in range(N)]
    P = int(input())
    p_number_list = [int(input()) for _ in range(P)]

    print_list = list()

    for p in p_number_list:
        bus_line = 0
        for ai, bi in n_number_list:
            if ai <= p <= bi:
                bus_line += 1
        print_list.append(bus_line)

    print(f"#{tc}", *print_list)
