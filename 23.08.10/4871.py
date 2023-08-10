T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    trunk_line_list = list()

    for _ in range(E):
        trunk_line_list.extend(map(int, input().split()))

    S, G = map(int, input().split())

    start_point = S
    stack = list()
    visited = [0] * V

    while start_point != G:
        for trunk_idx in range(len(trunk_line_list) // 2):
            if start_point == trunk_line_list[2 * trunk_idx] and visited[trunk_line_list[2 * trunk_idx + 1] - 1] == 0:
                stack.append(start_point)
                start_point = trunk_line_list[2 * trunk_idx + 1]
                break
        else:
            if stack:
                formal_point = stack.pop(-1)
                visited[start_point - 1] = 1
                start_point = formal_point
            else:
                break

    if start_point == G:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
