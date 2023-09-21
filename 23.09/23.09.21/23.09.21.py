# 18912
"""
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(a ,b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa


for i in range(n):
    for j in range(i + 1, n):
        if arr[i][j] == 0:
            continue
        if find(i) == find(j):
            print("WARNING")
            exit()
        union(i, j)
print("STABLE")
"""

# 18908

"""
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa < pb:
        parent[pb] = parent[pa]
    else:
        parent[pa] = parent[pb]


T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    eges = sorted([list(map(int, input().split())) for _ in range(e)], key=lambda x: x[2])
    parent = [i for i in range(v + 1)]
    total_v = 0
    cnt = 0

    for i in range(e):
        if cnt == v:
            break
        s, e, w = eges[i]
        if find(s) == find(e):
            continue
        union(s, e)
        total_v += w
    print(f"#{tc} {total_v}")
"""

# 18909

"""
from collections import deque


def bfs(r, c):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited[r][c] = 0
    que = deque()
    que.append((r, c))
    while que:
        r, c = que.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                val = 0
                if arr[nr][nc] > arr[r][c]:
                    val = arr[nr][nc] - arr[nr][nc]
                if visited[r][c] + 1 + val < visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1 + val
                    que.append((nr, nc))

    return visited[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float("inf")] * N for _ in range(N)]
    bfs(0, 0)
    print(f"#{tc} {visited[N - 1][N - 1]}")
"""

#

import heapq
node, edge = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [float("inf") * node]
visited = [False] * node
pq = []

for _ in range(edge):
    from_node, to, cost = map(int, input().split())
    graph[from_node].append((to, cost))


def dijkstra:
    distance[0] = 0
    heapq.heappush(pq, (0, 0))
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        for next_node, edge_cost in graph[cur_node]:
            total_cost = cur_cost + edge_cost
            if distance[next_node] > total_cost:
                distance[next_node] = total_cost
                heapq.heappush(pq, (distance[next_node], next_node))


dijkstra()
if distance[node - 1] == float("inf"):
    print("impossible")
else:
    print(distance[node - 1])