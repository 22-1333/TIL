T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = list()

    for n in range(N):
        row = list(map(int, input()))

        if 2 in row:
            start = n, row.index(2)

        maze.append(row)

    visited = list()
    complete = False


    def exiting(y, x):
        global complete

        if complete is False:
            visited.append((y, x))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for y_dir, x_dir in directions:
                if 0 <= y + y_dir < N and 0 <= x + x_dir < N:
                    if maze[y + y_dir][x + x_dir] == 0 or maze[y + y_dir][x + x_dir] == 2:
                        if (y + y_dir, x + x_dir) not in visited:
                            exiting(y + y_dir, x + x_dir)
                    elif maze[y + y_dir][x + x_dir] == 3:
                        complete = True


    exiting(start[0], start[1])

    if complete:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
