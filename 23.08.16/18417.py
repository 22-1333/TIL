N, M = map(int, input().split())
hand = list(map(int, input().split()))
picked = []
number_list = [n for n in range(1, N + 1)]
min_value = 9 ** M
min_list = [9] * M


def pick(m, p):
    global min_value
    if m == 0:
        value = 1
        for idx in p:
            value *= hand[idx - 1]
        if value < min_value:
            min_value = value
            for min_idx in range(len(p)):
                min_list[min_idx] = hand[p[min_idx] - 1]
        return
    else:
        if p:
            for not_picked in range(p[-1] + 1, N + 1):
                p.append(not_picked)
                pick(m - 1, p)
                p.pop()
        else:
            for not_picked in range(1, N + 1):
                p.append(not_picked)
                pick(m - 1, p)
                p.pop()


pick(M, picked)
print(*sorted(min_list))
