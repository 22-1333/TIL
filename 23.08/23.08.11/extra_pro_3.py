index = int(input())
evidence = [-1, 0, 0, 1, 2, 4, 4]
time_stamp = [8, 3, 5, 6, 8, 9, 10]
traces = list()


def dfs(start):
    if start != -1:
        traces.append([start, time_stamp[start]])
        dfs(evidence[start])
    else:
        return


dfs(index)

for trace in traces[::-1]:
    if trace[0] == 0:
        print("0번 index(출발)")
    else:
        print(f"{trace[0]}번 index({trace[1]}시)")
