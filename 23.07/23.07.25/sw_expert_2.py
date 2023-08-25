T = int(input())

for test_case in range(1, T + 1):
    v, e, v_1, v_2 = map(int, input().split())
    tree_route = list(map(int, input().split()))

    start_list = []
    end_list = []

    for n in range(len(tree_route)):
        if n % 2 == 0:
            start_list.append(tree_route[n])
        else:
            end_list.append(tree_route[n])
    
    if v_1 > v_2:
        v_1, v_2 = v_2, v_1

    start_point_1 = v_1
    short_way = []

    while start_point_1 != 1:
        short_way.append(start_point_1)
        start_point_1 = start_list[end_list.index(start_point_1)]
    short_way.append(1)

    start_point_2 = v_2
    long_way = []

    while start_point_2 != 1:
        long_way.append(start_point_2)
        start_point_2 = start_list[end_list.index(start_point_2)]
    long_way.append(1)

    for way in short_way:
        if way in long_way:
            ancestor = way
            break

    if ancestor == 1:
        count_descendants = v

    else:

        descendants_list = [] 

        start_list = start_list[::-1]
        end_list = end_list[::-1]


        for l in range(len(end_list)):
            each_way = []
            start_point_3 = end_list[l]

            while start_point_3 != 1:
                each_way.append(start_point_3)
                start_point_3 = start_list[end_list.index(start_point_3)]

            each_way.append(1)

            if ancestor in each_way:
                descendants_list.append(end_list[-l])

        count_descendants = len(descendants_list)

    print(f"#{test_case} {ancestor} {count_descendants}")
