S = int(input())
D = int(input())

queue = [S]
channel_list = [0] * 100001
is_found = False


def next_channel_list(previous):
    return [previous // 2, previous * 2, previous + 1, previous - 1]


while queue:
    if is_found:
        break
    else:
        now = queue.pop(0)

        for next_channel in next_channel_list(now):
            if 0 <= next_channel <= 100000 and channel_list[next_channel] == 0:
                queue.append(next_channel)
                channel_list[next_channel] = channel_list[now] + 1

                if next_channel == D:
                    is_found = True
                    break

print(channel_list[D])
