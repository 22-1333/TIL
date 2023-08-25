T = int(input())
for tc in range(1, T + 1):
    puzzle_list = [list(map(int, input().split())) for _ in range(9)]
    is_wrong = False

    for j in range(9):
        if len(set(puzzle_list[j])) != 9:
            is_wrong = True
            break

        check_set = set()
        for i in range(9):
            check_set.add(puzzle_list[i][j])
        if len(check_set) != 9:
            is_wrong = True
            break

    for j in range(3):
        for i in range(3):
            check_set = set()
            for dj in range(3):
                for di in range(3):
                    check_set.add(puzzle_list[j * 3 + dj][i * 3 + di])
            if len(check_set) != 9:
                is_wrong = True
                break

    if is_wrong:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1")
