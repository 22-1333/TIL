T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city_list = list()
    house_list = list()

    for j in range(N):
        row = list(map(int, input().split()))
        for i in range(N):
            if row[i] == 1:
                house_list.append((j, i))

        city_list.append(row)

    if N % 2 == 0:
        k_range = N + 2
    else:
        k_range = N + 1

    max_house = 0

    for k in range(1, k_range):
        operating_cost = k ** 2 + (k - 1) ** 2
        for y in range(-(k // 2), N + k):
            for x in range(-(k // 2), N + k):
                house = 0
                queue = [(y, x, 1)]
                visited = [(y, x)]

                while queue:
                    now_y, now_x, now_k = queue.pop(0)
                    if now_k < k:
                        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                        for dy, dx in directions:
                            if (now_y + dy, now_x + dx) not in visited:
                                queue.append((now_y + dy, now_x + dx, now_k + 1))
                                visited.append((now_y + dy, now_x + dx))
                                if (now_y + dy, now_x + dy) in house_list:
                                    house += 1

                if house * M >= operating_cost:
                    max_house = max(max_house, house)

    print(max_house)


