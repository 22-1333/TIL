import copy


def make_list(n, former_list):
    next_list = []

    global N

    while n != N:
    
        for former in former_list:
            for count in range(n + 1):                
                former_copy = copy.deepcopy(former)
                former_copy.insert(count, n + 1)

                next_list.append(former_copy)

        return make_list(n + 1, next_list)

    if n == N:

        return former_list

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    locations = list(map(int, input().split()))

    company_loc_x = locations.pop(2)
    company_loc_y = locations.pop(2)

    locations.append(company_loc_x)
    locations.append(company_loc_y)

    all_cases = make_list(1, [[1]])

    shortest_distance = None

    for case in all_cases:
        distance_total = 0
        start = 0
        end = 0
        for case_number in case:
            end = 2 * case_number
            distance = abs(locations[start] - locations[end]) + abs(locations[start + 1] - locations[end + 1])

            distance_total += distance

            start = end
        
        distance = abs(locations[start] - locations[-2]) + abs(locations[start + 1] - locations[-1])
        distance_total += distance

        print(distance_total)

        if shortest_distance == None:
            shortest_distance = distance_total
        else:
            shortest_distance = min(distance_total, shortest_distance)

print(shortest_distance)
