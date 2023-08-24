T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    is_five = False


    def right_diagonal(q, p):
        five = 0
        while 0 <= q < N and 0 <= p < N:
            if board[q][p] == "o":
                q += 1
                p += 1
                five += 1
            else:
                break
        if five >= 5:
            return True


    def left_diagonal(q, p):
        five = 0
        while 0 <= q < N and 0 <= p < N:
            if board[q][p] == "o":
                q -= 1
                p += 1
                five += 1
            else:
                break
        if five >= 5:
            return True


    for b in range(N):
        if is_five:
            break
        for a in range(N):
            if left_diagonal(b, a):
                is_five = True
                break
            if right_diagonal(b, a):
                is_five = True
                break

    for j in range(N):
        if is_five:
            break
        x = 0
        length = 0
        while x != N:
            if x == N - 1:
                if board[j][x] == "o":
                    if length + 1 >= 5:
                        is_five = True
                        break
                else:
                    if length >= 5:
                        is_five = True
                        break
                break
            elif board[j][x] == ".":
                if length >= 5:
                    is_five = True
                    break
                x += 1
                length = 0
            else:
                x += 1
                length += 1

    for i in range(N):
        if is_five:
            break
        y = 0
        length = 0
        while y != N:
            if y == N - 1:
                if board[y][i] == "o":
                    if length + 1 >= 5:
                        is_five = True
                        break
                else:
                    if length >= 5:
                        is_five = True
                        break
                break
            elif board[y][i] == ".":
                if length >= 5:
                    is_five = True
                y += 1
                length = 0
            else:
                y += 1
                length += 1

    if is_five:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")
