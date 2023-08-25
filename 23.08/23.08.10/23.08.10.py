# dsp

"""
V E
v1 w1 v2 w2
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 6 7 3 7


def dfs(n, V, adj_m):
    stack = list()  # stack 생성
    visited = [0] * (V + 1)  # visited 생성
    visited[n] = 1  # 시작점 방문 표시
    print(n)  # do[n]
    while True:
        for w in range(1, V):  # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)  # push(n), v = w
                n = w
                print(n)  # do(w)
                visited[n]  # w 방문 표시
                break
        else:
            if stack:  # 스택에 지나온 정점이 남아있으면
                n = stack.pop()  # pop() 해서 다시 다른 w를 찾을 n 준비
            else:  # 스택이 비어있으면
                break
    return


V, E = map(int, input().split())  # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0]*(V + 1) for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1
"""

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
