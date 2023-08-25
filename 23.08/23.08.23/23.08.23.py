# 1289
"""
T = int(input())

for tc in range(1, T + 1):
    cnt = 0
    now = "0"
    num = input()
    for i in range(len(num)):
        if num[i] != now:
            cnt += 1
            now = num[i]

    print(f"#{tc} {cnt}")
"""

# 6485

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stop = [0] * 5001
    for i in range(N):
        Ai, Bi = map(int, input().split())
        for j in range(Ai, Bi + 1):
            stop[j] += 1
    P = int(input())
    result = list()
    for j in range(P):
        Cj = int(input())
        result.append(stop(Cj))
    print(f"#{tc}", *result)
"""

# 1979
"""
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N - 1:
                if cnt == K:
                    result += 1
                cnt = 0
    print(f"#{tc} {cnt}")
"""

# 11315

"""
def omok():
    dy = [1, 0, 1, -1]
    dx = [0, 1, 1, 1]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == "o":
                for direction in range(4):
                    ny = y
                    nx = x
                    cnt = 0
                    while 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == "o":
                        cnt += 1
                        ny += dy[direction]
                        nx += dx[directino]
                    if cnt >= 5:
                        return "YES"
    return "NO"


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input()]
    print(f"#{tc} {omok()}")
"""

# 18610

"""
def find(node):
    if node != root[node]:
        root[node] = find(root[node])
    return root[node]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if rank[root_x] > rank[root_y]:
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1


N, Q = map(int, input().split())
rank = [0] * (N + 1)
root = [i for i in range(N + 1)]
for _ in range(Q):
    K, A, B = map(int, input().split())
    if K == 0:
        if find(A) == find(B):
            print("YES")
        else:
            print("NO")
    else:
        union(A, B)
"""
