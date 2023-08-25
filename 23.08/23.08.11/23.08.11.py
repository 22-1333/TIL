# 1974

"""
def sudoku(arr):
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:  # 1~9에 빠진 숫자가 있으면
                return 0  # 0 리턴


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = sudoku(arr)
    print(f"#{tc} {ans}")
"""

# 1234

"""
T = 10
for tc in range(1, T + 1):
    str_N, str_num = input().split()

    N = int(str_N)
    stack = [0] * N
    top = -1

    for t in str_num:
        if top == -1 or stack[top] != t:  # 스택이 비어있거나, top 원소와 다르면
            top += 1  # push(t)
            stack[top] = t
        else:  # 스택이 비어있지 않고, top 과 같으면
            top -= 1
    ans = "".join(stack[:top + 1])
    print(f"#{tc} {''.join(stack[:top + 1])}")
"""

# extra_pro_1

"""
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def dfs(now):
    # 현재 방문한 노드 출력
    print(now, end=" ")
    for i in range(N):
        # now 와 i 번째 노드가 연결되어 있다면
        if arr[now][i] == 1:
            # 재귀적으로 i 번째 노드 방문
            dfs(i)


dfs(0)
"""

# extra_pro_2

"""
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * 3


def dfs(now, level):
    global visited
    visited[level] = str(now)
    if level == 2:
        print(" ".join(visited))
    for i in range(N):
        if arr[now][i] == i:
            dfs(i, level + 1)


dfs(0, 0)
"""

# extra_pro_3

"""
evidence = [-1, 0, 0, 1, 2, 4, 4]
time_stamp = [8, 3, 5, 6, 8, 9, 10]

N = int(input())


def dfs(idx, time):
    if evidence[idx] == -1:
        print(f"{idx}번 index(출발)")
        return
    
    dfs(evidence[idx], time_stamp[idx])
    print(f"{idx}번 index({time_stamp[idx]}시)")
    

dfs(n, time_stamp[n])
"""

# extra_pro_4

"""
N = int(input())
M = int(input())
arr = [[0] * N for _ in range(N)]
visited = [0] * N
for _ in range(M):
    c1, c2 = map(int, input().split())
    arr[c1 - 1][c2 - 1] = arr[c2 - 1][c1 - 1] = 1


def dfs(v):
    visited[v] = 1
    for i in range(N):
        if arr[v][i] == 1 and not visited[i]:
            dfs(i)


dfs(0)
print(sum(visited) - 1)
"""
