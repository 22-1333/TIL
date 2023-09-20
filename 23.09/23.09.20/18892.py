N = int(input())
decoration_dict = dict()
for _ in range(N):
    deco, deco_l, deco_r = list(map(int, input().split()))
    decoration_dict[deco] = [deco_l, deco_r]

pattern_1_list = list()
pattern_2_list = list()
pattern_3_list = list()


def pattern_1(now):
    visited = [0] * N
    if now == -1:
        return

    left, right = decoration_dict[now]

    if left == -1 and right == -1:
        pattern_1_list.append(now)
        return
    else:
        pattern_1(left)
        pattern_1_list.append(now)
        pattern_1(right)


def pattern_2(now):
    if now == -1:
        return

    left, right = decoration_dict[now]

    if left == -1 and right == -1:
        pattern_2_list.append(now)
        return
    else:
        pattern_2_list.append(now)
        pattern_2(left)
        pattern_2(right)


def pattern_3(now):
    if now == -1:
        return

    left, right = decoration_dict[now]

    if left == -1 and right == -1:
        pattern_3_list.append(now)
        return
    else:
        pattern_3(left)
        pattern_3(right)
        pattern_3_list.append(now)


pattern_1(1)
pattern_2(1)
pattern_3(1)
print(*pattern_1_list)
print(*pattern_2_list)
print(*pattern_3_list)
