import itertools

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    locations = list(map(int, input().split()))

    company_loc_x = locations.pop(2)
    company_loc_y = locations.pop(2)

    start_loc_x = locations.pop(0)
    start_loc_y = locations.pop(0)

    shortest_distance = None

    all_cases = list(itertools.permutations(list(n for n in range(N))))

    for case in all_cases:
        
        start_x = start_loc_x
        start_y = start_loc_y

        distance_total = 0

        for case_number in case:
            end_x = locations[case_number * 2]
            end_y = locations[case_number * 2 + 1]

            distance = abs(start_x - end_x) + abs(start_y - end_y)

            distance_total += distance

            start_x = end_x
            start_y = end_y

        end_x = company_loc_x
        end_y = company_loc_y

        distance = abs(start_x - end_x) + abs(start_y - end_y)
        distance_total += distance

        if shortest_distance is None:
            shortest_distance = distance_total
        else:
            shortest_distance = min(distance_total, shortest_distance)

    print(f"#{tc} {shortest_distance}")
