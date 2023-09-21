N = int(input())
adj_list = [list(map(int, input().split())) for _ in range(N)]
first = False

for node in range(N):
    if adj_list[node].count(1) == 1:
        first = node
        break


def circuit(start):
    visited = [0] * N
    visited[start] = 1
    queue = [(start, start)]

    while queue:
        before, now = queue.pop(0)

        for next_node, is_connected in enumerate(adj_list[now]):
            if is_connected and next_node != before:
                if visited[next_node]:
                    return "WARNING"
                else:
                    queue.append((now, next_node))
                    visited[next_node] = 1

    return "STABLE"


if first is False:
    print("WARNING")
else:
    print(circuit(first))
