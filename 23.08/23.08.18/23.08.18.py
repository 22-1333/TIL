# 5105

"""
def bfs(sti, stj, n):
    visited = [[0] * N for _ in range(N)]
    queue = list()
    queue.append((sti, stj))
    visited[sti][stj] = 1
    while queue:
        i, j = queue.pop(0)
        if maze[i][j] == 3:
            return visited[i][j] - 2

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    return 0


def find_start(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    st_i, st_j = find_start(N)
    ans = bfs(st_i, st_j, N)
    print(f"#{tc} {ans}")
"""

# 5099

"""
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))
    pizzas = [[i + 1, p] for i, p in enumerate(cheeses)]
    oven = pizzas[:N]
    remain = pizzas[N:]

    while len(oven) > 1:
        now = oven.pop(0)
        now[1] //= 2
        if now[1] == 0:
            if remain:
                oven.append(remain.pop(0))
        else:
            oven.append(now)
    
    print(f"#{tc} {oven[0][0]}")
"""

# 5102

"""
from collections import deque


def bfs(start, end):
    queue = deque([(start, 0)])
    while queue:
        n, cnt = queue.popleft()
        
        if not visited[n]:
            visited[n] = 1
        
        for j in arr[n]:
            if not visited[j] and j == end:
                return cnt + 1
            elif not visited[j]:
                queue.append((j, cnt + 1))
    
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        n1, n2 = map(int, input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)
    S, G = map(int, input().split())
    print(f"#{tc} {bfs(S, G)}")
"""

# 18444

"""
from collections import deque


def bfs(start, target):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for i in range(1, N + 1):
            if arr[now][i] == 0:
                continue
            if visited[i] == 1:
                continue
            if i == target:
                print("YES")
                return
            queue.append(i)
            visited[i] = 1
    print("NO")


N = int(input())
T = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(T):
    A, B = map(int, input().split())
    arr[A][B] = 1
    arr[B][A] = 1

coco = int(input())
coco_target = int(input())
bfs(coco, coco_target)
"""

# 18445

"""
from collections import deque
N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    arr[A][B] = 1
    arr[B][A] = 1
R, K = map(int, input().split())
cnt = 0


def bfs(node):
    global cnt
    queue = deque()
    queue.append(node)
    visited[node] = 1
    while 1:
        now = queue.popleft()
        if visited[now] - 1 <= K:
            cnt += 1
        if visited[now] - 1 > K:
            break
        for i in range(1, N + 1):
            if arr[now][i] == 0:
                continue
            if visited[i] > 0:
                continue
            visited[i] = visited[now] + 1
            queue.append(i)


bfs(R)
print(cnt)
"""
