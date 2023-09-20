import copy

N, robot_1, robot_2 = map(int, input().split())
passageway_list = [list(map(int, input().split())) for _ in range(N - 1)]
distance_list = list()


def dfs(before, now, distance):
    global distance_list

    if now == robot_2:
        distance_list = distance
        return

    for room_1, room_2, length in passageway_list:
        if room_1 == now:
            if room_2 != before:
                next_distance = copy.deepcopy(distance)
                next_distance.append(length)
                dfs(now, room_2, next_distance)
        if room_2 == now:
            if room_1 != before:
                next_distance = copy.deepcopy(distance)
                next_distance.append(length)
                dfs(now, room_1, next_distance)


dfs(0, robot_1, [])
print(sum(distance_list) - max(distance_list))
