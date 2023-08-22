T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    leaf_node_list = [list(map(int, input().split())) for _ in range(M)]
    node_list = [0] * (N + 1)


    def node(number_l):
        if node_list[number_l]:
            return node_list[number_l]
        else:
            if number_l * 2 <= N:
                if number_l * 2 + 1 <= N:
                    node_list[number_l] = node(number_l * 2) + node(number_l * 2 + 1)
                    return node(number_l * 2) + node(number_l * 2 + 1)
                else:
                    node_list[number_l] = node(number_l * 2)
                    return node(number_l * 2)
            else:
                for leaf_node in leaf_node_list:
                    if number_l == leaf_node[0]:
                        node_list[number_l] = leaf_node[1]
                        return leaf_node[1]


    print(f"#{tc} {node(L)}")
