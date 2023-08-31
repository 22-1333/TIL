T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time_list = [list(map(int, input().split())) for _ in range(N)]
    time_list.sort(reverse=True)
    truck_list = [0] * N
    max_truck = 0

    for idx in range(N):
        if not truck_list[idx]:
            truck_list[idx] = 1
            queue = [(idx, truck_list[idx])]
            while queue:
                now_idx, now_truck = queue.pop(0)
                if truck_list[now_idx]:
                    max_truck = max(max_truck, now_truck + truck_list[now_idx])
                else:
                    for before_idx in range(0, idx):
                        before_s, before_e = time_list[before_idx]
                        if time_list[now_idx][0] >= before_e:
                            queue.append((before_idx))

    print(f"#{tc} {max_truck}")
