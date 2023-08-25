N, Q = map(int, input().split())
query_list = [list(map(int, input().split())) for _ in range(Q)]
group_list = list()

for query in query_list:
    queue = list()
    if query[0] == 1:
        for group in group_list:
            if query[1] in group or query[2] in group:
                group.add(query[1])
                group.add(query[2])
                break
        else:
            new_group = set()
            new_group.add(query[1])
            new_group.add(query[2])
            group_list.append(new_group)
    else:
        for group in group_list:
            if query[1] in group and query[2] in group:
                print("YES")
                break
        else:
            print("NO")
