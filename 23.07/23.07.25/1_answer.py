def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) + abs(y1 - y2)


def tsp_dp(start, end, waypoints):
    coords = [start] + waypoints + [end]
    n = len(coords)

    dp = [[None] * n for _ in range(2 ** n)]

    visited_all = (1 << n) - 1

    def tsp_dp_helper(mask, pos):
        if mask == visited_all:
            return distance(coords[pos], end)

        if dp[mask][pos] is not None:
            return dp[mask][pos]

        min_distance = float("inf")

        for next_pos in range(n):
            if (mask >> next_pos) & 1 == 0:
                new_mask = mask |(1 << next_pos)
                distance_to_next = distance(coords[pos], coords[next_pos])
                distance_to_end = tsp_dp_helper(new_mask, next_pos)
                total_distance = distance_to_next + distance_to_end
                min_distance = min(min_distance, total_distance)

        dp[mask][pos] = min_distance
        return min_distance

    min_distance = tsp_dp_helper(1, 0)

    return min_distance


T = int(input())
for i in range(1, T + 1):
    count = int(input())
    a_tuple = tuple(map(int, input().split()))
    a_list = [a_tuple[(2 * i):(2 * i + 2)] for i in range(len(a_tuple)//2)]
    start = a_list.pop(0)
    end = a_list.pop(0)
    waypoints = a_list

    min_distance = tsp_dp(start, end, waypoints)
    print(f"#{i} {min_distance}")
