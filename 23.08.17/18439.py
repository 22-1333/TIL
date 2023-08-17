def bfs(n):
    visited = list()
    for y, x in adj_matrix:
        if y == n and x not in used:
            print(x)
            visited.append(x)
    else:
        if visited:
            used.extend(visited)
            for visited_x in visited:
                bfs(visited_x)
        else:
            return


N = int(input())
adj_matrix = [(0, 4), (1, 0), (1, 2), (1, 5), (2, 0), (2, 3), (3, 0), (3, 1), (4, 1), (4, 3), (4, 5), (5, 2), (5, 3)]
used = [N]
print(N)
bfs(N)
