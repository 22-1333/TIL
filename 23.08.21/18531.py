T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    town_map = list()
    home = 0
    for n in range(N + 1):
        row = list(map(int, input().split()))
        home += row.count(1)
        town_map.append(row)
        if 2 in row:
            m = row.index(2)
            repeater_y, repeater_x = (n, m)

    r = 0
    within = 0
    while within != home:
        within = 0
        r += 1
        for dx in range(-r, r + 1):
            y_range = int((r ** 2 - dx ** 2) ** 0.5)
            for dy in range(-y_range, y_range + 1):
                if 0 <= dy + repeater_y <= N and 0 <= dx + repeater_x <= N:
                    if town_map[dy + repeater_y][dx + repeater_x] == 1:
                        within += 1

    print(f"#{tc} {r}")
