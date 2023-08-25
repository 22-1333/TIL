T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())
    virus_list = [list(map(int, input().split())) for _ in range(N)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_virus = None

    for y in range(N):
        for x in range(N):
            virus = virus_list[y][x]
            for p in range(1, P + 1):
                for dy, dx in directions:
                    if 0 <= y + dy * p < N and 0 <= x + dx * p < N:
                        virus += virus_list[y + dy * p][x + dx * p]
            try:
                max_virus = max(max_virus, virus)
            except TypeError:
                max_virus = virus

    print(f"#{tc} {max_virus}")
