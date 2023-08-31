T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    cargo = 0

    for truck in T:
        max_weight = 0
        max_idx = -1
        for i in range(N):
            if W[i] <= truck and W[i] != 0:
                if W[i] > max_weight:
                    max_weight = W[i]
                    max_idx = i
        if max_idx != -1:
            W[max_idx] = 0
        cargo += max_weight

    print(f"#{tc} {cargo}")

