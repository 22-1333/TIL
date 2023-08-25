T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    grid = dict()
    for n in range(N):
        row = list(map(int, input().split()))
        for m in range(len(row)):
            if row[m] != 0:
                grid[(n, m)] = row[m], row[m]


    def reproduction(y, x):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dy, dx in directions:
            if (y + dy, x + dx) not in grid:
                if (y + dy, x + dx) in new_grid:
                    if new_grid[(y + dy, x + dx)][0] < grid[(y, x)][0]:
                        new_grid[(y + dy, x + dx)] = grid[(y, x)][0], grid[(y, x)][0]
                else:
                    new_grid[(y + dy, x + dx)] = grid[(y, x)][0], grid[(y, x)][0]

    for k in range(K + 1):
        new_grid = dict()
        for grid_y, grid_x in grid:
            if -grid[(grid_y, grid_x)][0] <= grid[grid_y, grid_x][1]:
                grid[(grid_y, grid_x)] = grid[(grid_y, grid_x)][0], grid[(grid_y, grid_x)][1] - 1
        for grid_y, grid_x in grid:
            if -grid[(grid_y, grid_x)][0] <= grid[(grid_y, grid_x)][1] < 0:
                reproduction(grid_y, grid_x)

        grid.update(new_grid)

    stem = 0
    for grid_cell in grid:
        if grid[grid_cell][1] >= -grid[grid_cell][0]:
            stem += 1

    print(stem)
