T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    number_list = list(map(int, input().split()))
    binary_tree = [0]
    last = 0

    for number in number_list:
        binary_tree.append(number)
        last += 1
        test = last

        while binary_tree[test // 2] != 0:
            if binary_tree[test // 2] > binary_tree[test]:
                binary_tree[test // 2], binary_tree[test] = binary_tree[test], binary_tree[test // 2]

            test //= 2

    node_sum = 0
    child_node = last

    while binary_tree[child_node // 2] != 0:
        node_sum += binary_tree[child_node // 2]
        child_node //= 2

    print(f"#{tc} {node_sum}")
