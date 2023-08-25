Computer = int(input())
Pair = int(input())
pair_list = [list(map(int, input().split())) for _ in range(Pair)]

start = 1
visited = [False] * Computer
virus_computer = list()


def dfs(now):
    visited[now - 1] = True
    for pair in pair_list:
        if now in pair:
            if pair.index(now) == 0:
                to_index = 1
            else:
                to_index = 0
            to = pair[to_index]

            if visited[to - 1] is False:
                virus_computer.append(to)
                visited[to - 1] = True
                dfs(to)


dfs(1)
print(len(virus_computer))
