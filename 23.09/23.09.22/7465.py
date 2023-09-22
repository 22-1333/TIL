T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    relationships = [list(map(int, input().split())) for _ in range(M)]
    parent = [n for n in range(1, N + 1)]


    def union(a, b):
        if parent[b - 1] > parent[a - 1]:
            a, b = b, a
        if parent[a - 1] > parent[b - 1]:
            a_parent = parent[a - 1]
            for idx in range(N):
                if parent[idx] == a_parent:
                    parent[idx] = parent[b - 1]


    for relationship in relationships:
        print(relationship)
        union(relationship[0], relationship[1])
        print(parent)

    parent = set(parent)
    print(f"#{tc} {len(parent)}")
