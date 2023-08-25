T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    left = 1
    right = P
    c = int((left + right) / 2)
    a_cnt = 1

    while c != Pa:
        a_cnt += 1

        if c < Pa:
            left = c
            c = int((left + right) / 2)
        else:
            right = c
            c = int((left + right) / 2)

    left = 1
    right = P
    c = int((left + right) / 2)
    b_cnt = 1

    while c != Pb:
        b_cnt += 1

        if c < Pb:
            left = c
            c = int((left + right) / 2)
        else:
            right = c
            c = int((left + right) / 2)

    if a_cnt > b_cnt:
        winner = "B"
    elif a_cnt == b_cnt:
        winner = "0"
    else:
        winner = "A"

    print(f"#{tc}", winner)
