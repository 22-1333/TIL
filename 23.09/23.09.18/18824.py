def binary_search(target):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if relative_strength_list[mid] > target:
            end = mid - 1
        elif relative_strength_list[mid] < target:
            start = mid + 1
        elif relative_strength_list[mid] == target:
            return True

    return False


N, Q = map(int, input().split())
relative_strength_list = sorted(list(map(int, input().split())))
for _ in range(Q):
    Si, Ei = map(int, input().split())
