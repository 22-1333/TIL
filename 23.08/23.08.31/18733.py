N = int(input())
weight_list = list(map(int, input().split()))


def dough(slimes):
    if len(slimes) == 2:
        return sum(slimes)
    for a in range(len(slimes)):
        for b in range(a, len(slimes)):
            if a != b:
                next_slimes =