# 4871

"""
T = int(input())


def dfs(start, end):
    stack = []
    visited = [False] * (V + 1)
    stack.append(start)

    while stack:
        now = stack.pop()
        visited[now] = True
        for following in range(1, V + 1):
            if node[now][following] and not visited[following]:
                stack.append(following)
    if visited[end]:
        return 1
    else:
        return 0


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    node = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        input_start, input_end = (map(int, input().split()))
        node[input_start][input_end] = 1
    S, G = map(int, input().split())
    print(f"#{tc} {dfs(S, G)}")
"""

# 4873

"""
T = int(input())
for tc in range(1, T + 1):
    string = list(input())
    stack = []
    for char in string:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    print(f"#{tc} {len(stack)}")
"""
