T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    red_painting = set()
    blue_painting = set()
    purple_painting = set()

    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        if color == 1:
            for x in range(r1, r2 + 1):
                for y in range(c1, c2 + 1):
                    red_painting.add((x, y))
        else:
            for x in range(r1, r2 + 1):
                for y in range(c1, c2 + 1):
                    blue_painting.add((x, y))

    purple_painting = red_painting & blue_painting
    count = 0

    for painting in purple_painting:
        count += 1

    print(f"#{tc} {count}")
