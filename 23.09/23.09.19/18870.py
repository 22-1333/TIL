def m_1(index):
    if index == N:
        print(*base)
        return
    for dice_number in range(1, 7):
        base[index] = dice_number
        m_1(index + 1)


def m_2(index, min_dice_num):
    if index == N:
        print(*base)
        return
    for dice_number in range(min_dice_num, 7):
        base[index] = dice_number
        m_2(index + 1, dice_number)


def m_3(index):
    if index == N:
        print(*base)
        return
    for dice_number in range(1, 7):
        if dice[dice_number - 1] == 0:
            dice[dice_number - 1] = 1
            base[index] = dice_number
            m_3(index + 1)
            dice[dice_number - 1] = 0
        else:
            continue


N, M = map(int, input().split())
base = [1] * N
dice = [0] * 6

if M == 1:
    m_1(0)
elif M == 2:
    m_2(0, 1)
elif M == 3:
    m_3(0)