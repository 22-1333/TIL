def binary_search(target):
    start, end = 0, N
    while start <= end:
        mid = (start + end) // 2
        if A[mid] > target:
            end = mid - 1
        elif A[mid] < target:
            start = mid + 1
        elif A[mid] == target:
            return True

    return False


N = int(input())
A = sorted(list(map(int, input().split())))
K = int(input())
B = list(map(int, input().split()))
for b in B:
    if binary_search(b):
        print("O", end="")
    else:
        print("X", end="")