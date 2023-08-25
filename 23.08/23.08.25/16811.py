T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))
    Ci.sort()
    min_diff = None
    min_carrot = False

    for first_idx in range(1, len(Ci) - 1):
        if Ci[first_idx - 1] == Ci[first_idx]:
            continue
        else:
            for second_idx in range(first_idx + 1, len(Ci)):
                if Ci[second_idx - 1] == Ci[second_idx]:
                    continue
                else:
                    small = len(Ci[:first_idx])
                    middle = len(Ci[first_idx:second_idx])
                    big = len(Ci[second_idx:])
                    box = [small, middle, big]
                    if 0 not in box and max(box) <= (N // 2):
                        min_carrot = True
                        diff = abs(small - middle)
                        for idx_1, idx_2 in [(1, 2), (0, 2)]:
                            diff = max(diff, abs(box[idx_1] - box[idx_2]))

                        try:
                            min_diff = min(min_diff, diff)
                        except TypeError:
                            min_diff = diff

    if min_carrot:
        print(f"#{tc} {min_diff}")
    else:
        print(f"#{tc} -1")
