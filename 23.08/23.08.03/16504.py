T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_drop = 0

    for idx in range(len(arr)):
        drop = N - idx - 1
        for taller_idx in range(idx + 1, len(arr)):
            if arr[idx] <= arr[taller_idx]:
                drop -= 1
        if max_drop < drop:
            max_drop = drop

    print(f"#{tc} {max_drop}")
