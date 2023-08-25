def double(code):
    return (code * 2) % 10000


def subtract(code):
    if code == 0:
        return 9999
    else:
        return code - 1


def left_rotate(code):
    return (code % 1000) * 10 + (code // 1000)


def right_rotate(code):
    return (code % 10) * 1000 + (code // 10)


N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    queue = [A]
    tries = 0

    while queue:
        now = queue.pop(0)
        if now == B:
            break
        else:
            queue.append(double(now))
            queue.append(subtract(now))
            queue.append(left_rotate(now))
            queue.append(right_rotate(now))
            tries += 1

    process = ""
    while tries > 0:
        if tries % 4 == 1:
            process += "D"
        elif tries % 4 == 2:
            process += "S"
        elif tries % 4 == 3:
            process += "L"
        elif tries % 4 == 0:
            tries -= 4
            process += "R"

        tries = tries // 4
    process = process[::-1]

    print(process)
