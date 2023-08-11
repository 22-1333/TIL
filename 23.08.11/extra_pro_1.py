N = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]

start = 0
visited = [0] * N
stack = list()

print(start, end=" ")

while True:
    for to in range(N):
        if adj_matrix[start][to] == 1 and visited[to] == 0:
            visited[to] = 1
            stack.append(start)
            start = to
            print(to, end=" ")
            break
    else:
        if stack:
            start = stack.pop()
        else:
            break
