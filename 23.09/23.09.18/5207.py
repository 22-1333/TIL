def binary_search(target):
    start, end = 0, N - 1
    direction = 0
    while start <= end:
        mid = (start + end) // 2
        if A[mid] > target:
            if direction == -1:
                return False
            else:
                end = mid - 1
                direction = -1
        elif A[mid] < target:
            if direction == 1:
                return False
            else:
                start = mid + 1
                direction = 1
        elif A[mid] == target:
            return True

    return False


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    counting = 0
    for b in B:
        if binary_search(b):
            counting += 1

    print(f"#{tc} {counting}")
