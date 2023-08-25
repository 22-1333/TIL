T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    charging = 0
    formal_sta = 0
    next_sta = K
    while next_sta < N:
        for idx in range(M - 1, -1, -1):
            if arr[idx] > next_sta:
                continue
            if arr[idx] > formal_sta:
                charging += 1
                formal_sta = arr[idx]
                next_sta = arr[idx] + K
                break
            else:
                charging = 0
        if charging == 0:
            break
    print(f"#{tc} {charging}")
