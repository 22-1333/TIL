T = int(input())
for tc in range(1, T + 1):
    Mi = list(map(int, input().split()))
    N = Mi.pop(0)
    now = 0
    change = 0
    is_end = False

    while now < N - 1:
        battery = Mi[now]
        max_move = 0
        for move in range(1, battery + 1):
            if now + move >= N - 1:
                is_end = True
                break
            else:
                if max_move < now + move + Mi[now + move]:
                    next_point = now + move
                    max_move = now + move + Mi[now + move]

        if is_end:
            break
        else:
            now = next_point

        change += 1

    print(f"#{tc} {change}")
