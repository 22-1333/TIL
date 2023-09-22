# 18910
"""
def dijkstra(start):
    dist[start] = 0
    for _ in range(N + 1):
        min_idx = -1
        min_value = float("inf")

        for i in range(N + 1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]

        visited[min_ids] = 1

        for i in range(N + 1):
            if arr[min_idx][i] and not visited[i]:
                dist[i] = min(dist[i], dist[min_idx] + arr[min_idx][i])


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    dist = [float("inf") for _ in range(N + 1)]
    for s, e, w in edges:
        arr[s][e] = w
    dijkstra(0)
    print(f"{tc} {dist[N]}")
"""

# 7465

"""
def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa > pb:
        pa, pb = pb, pa

    parents[pb] = pa


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parents = {i: i for i in range(1, N + 1)}
    for i in range(M):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a, b)
    group = set()
    for i in range(1, N + 1):
        if parents[i] not in group:
            x = find(i)
            if x not in group:
                group.add(x)
    print(f"#{tc} {len(group)}")
"""


# 1795

"""

"""

# 18922

"""
from heapq import heappush, heappop
n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
dist = [[float("inf")] * m for _ in range(n)]

y_dir = [0, 0, 1, -1]
x_dir = [-1, 1, 0, 0]


def dijkstra():
    pq = []
    dist[0][0] = MAP[0][0]
    heappush(pq, (MAP[0][0], 0, 0))
    while pq:
        cost, y, x = heappop(pq)
        if dist[y][x] < cost:
            continue
        for i in range(4):
            ny = y + y_dir[i]
            nx = x + x_dir[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            next_cost = cost + MAP[ny][nx]
            if dist[ny][nx] <= next_cost:
                continue
            dist[ny][nx] = next_cost
            heappush(pq, (next_cost, ny, nx))
    return dist[n - 1][m - 1]


print(dijkstra())
"""
