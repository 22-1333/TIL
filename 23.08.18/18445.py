N, M = map(int, input().split())
route_list = [list(map(int, input().split())) for _ in range(M)]
R, K = map(int, input().split())

queue = [R]
bus_number_list = [False] * N
bus_number_list[R - 1] = 0

while queue:
    start = queue.pop()
    for route in route_list:
        if start in route:
            start_idx = route.index(start)
            end = route[not start_idx]

            if bus_number_list[end - 1] is False:
                queue.append(end)
                bus_number_list[end - 1] = bus_number_list[start - 1] + 1

easy_to_go = 0
for bus_number in bus_number_list:
    if bus_number <= K and bus_number is not False:
        easy_to_go += 1

print(easy_to_go)
