M, N = map(int, input().split())
K = int(input())
bus_section = [list() for _ in range(K + 1)]
for _ in range(K):
    b, x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            bus_section[b].append([x, y])

sx, sy, dx, dy = map(int, input().split())
start = list()

for n in range(len(bus_section)):
    if [sx, sy] in bus_section[n]:
        start.append([sx, sy, n])

for start_x, start_y, start_bus in start:
    queue = [[start_x, start_y, start_bus, 1]]
    took = [0] * (K + 1)
    took[start_bus] = 1

    while queue:
        now_x, now_y, bus_number, transfer = queue.pop(0)
        for bus_stop_x, bus_stop_y in bus_section[bus_number]:
            if bus_stop_x == dx and bus_stop_y == dy:
                break
            else:
                for n in range(len(bus_section)):
                    if [bus_stop_x, bus_stop_y] in bus_section[n] and not took[n]:
                        queue.append([bus_stop_x, bus_stop_y, n, transfer + 1])
        else:
            continue
        break

    try:
        min_transfer = min(transfer, min_transfer)
    except NameError:
        min_transfer = transfer

print(min_transfer)
