def security_area(center_y, center_x, k_value):
    security_area_list = [(center_y, center_x)]
    for dx in range(1, k_value):
        security_area_list.append((center_y, center_x + dx))
        security_area_list.append((center_y, center_x - dx))

    for dy in range(1, k_value):
        security_area_list.append((center_y + dy, center_x))
        security_area_list.append((center_y - dy, center_x))
        for dx in range(1, k_value - dy):
            security_area_list.append((center_y + dy, center_x + dx))
            security_area_list.append((center_y - dy, center_x + dx))
            security_area_list.append((center_y + dy, center_x - dx))
            security_area_list.append((center_y - dy, center_x - dx))

    return security_area_list


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city_list = [list(map(int, input().split())) for _ in range(N)]
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
                for check_area_y, check_area_x in security_area(y, x, k):
                    if 0 <= check_area_y < N and 0 <= check_area_x < N:
                        if city_list[check_area_y][check_area_x] == 1:
                            house += 1

                if house * M >= operating_cost:
                    max_house = max(max_house, house)

    print(f"#{tc} {max_house}")
