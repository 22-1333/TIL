N, M = map(int, input().split())
route_list = [list(map(int, input().split())) for _ in range(M)]
T = int(input())

queue = [1]
transfers = [False] * (N + 1)
transfers[1] = 0
is_arrived = False

while queue:
    if is_arrived:
        break
    else:
        start = queue.pop(0)

        for route in route_list:
            if T in route:
                continue
            else:
                if start in route:
                    start_idx = route.index(start)
                    end = route[not start_idx]

                    if transfers[end] is False:
                        queue.append(end)
                        transfers[end] = transfers[start] + 1

                        if end == N:
                            is_arrived = True
                            break

if is_arrived:
    print(transfers[N])
else:
    print(-1)
