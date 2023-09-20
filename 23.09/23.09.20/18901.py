T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())


    def calculation(index, number):
        if index == 0:
            return number * 2
        elif index == 1:
            return number - 10
        elif index == 2:
            return number - 1
        elif index == 3:
            return number + 1


    queue = [(N, 0)]
    min_cal = 0
    pass_list = [0] * 1000001
    pass_list[N] = 1

    while queue:
        now, counting = queue.pop(0)

        if now == M:
            min_cal = counting
            break

        for idx in range(4):
            next_num = calculation(idx, now)
            if 0 <= next_num <= 1000000:
                if not pass_list[next_num]:
                    pass_list[next_num] = 1
                    queue.append((calculation(idx, now), counting + 1))

    print(f"#{tc} {min_cal}")
