T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    for m in range(M):
        first_num = num_list.pop(0)
        num_list.append(first_num)

    print(f"#{tc} {num_list[0]}")
