def bfs(n):
    visited = list()
    for y, x in adj_matrix:
        if y == n:
            visited.append(x)
    else:
        if visited:
            for visited_x in visited:
                print(visited_x, end=" ")
            else:
                k = visited.pop(0)
                bfs(k)
        else:
            return


adj_matrix = [(0, 1), (0, 4), (1, 2), (1, 5), (2, 3)]

N = int(input())
print(N, end=" ")
bfs(N)