# 4837

"""
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    result = 0
    # 1<<12 -> 이진수 1을 왼쪽으로 12비트 이동 -> 100000000000 -> 2 ** 12
    # arr 의 요소의 개수가 12개이기 때문
    for i in range(1 << 12):
        sum_sub = 0
        subset = []
        for j in range(12):
            # i의 j번째 비트가 1인지 아닌지 알 수 있다.
            # 12의 이진수 1100, 5의 이진수 0101 -> 1100 & 0101 -> 0100
            if i & (1 << j):  # i의 j번째 연산자가 1인지 아닌지 탐색하는 코드
                sum_sub += arr[j]
                subset.append(arr[j])
        if len(subset) == N and sum_sub == K:
            result += 1
    print(f"#{tc} {result}")
"""

# 4839

"""
def binary_search(pages, p):
    start = 1
    end = pages
    mid = 0
    cnt = 1

    # 만약 mid 이 p 와 같다면, 찾는 값 p 를 찾은 것이므로 탐색을 종료
    while p != mid:
        mid = (start + end) / 2
        if mid > p:
            end = mid
        else:
            start = mid
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    A = binary_search(P, Pa)
    B = binary_search(P, Pb)
    result = 0
    if A == B:
        result = 0
    elif A < B:
        result = "A"
    else:
        result = "B"
    print(f"#{tc} {result}")
"""

# 4843

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []

    while len(numbers) > 0:
        max_value = max(numbers)
        numbers.remove(max_value)
        result.append(max_value)

        min_value = min(numbers)
        numbers.remove(min_value)
        result.append(min_value)

    print(f"#{tc}", *result[:10])
"""

# extra_pro_1

"""
N, M = map(int, input().split())
K = int(input())
arr = [list(input()) for _ in range(N)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == "@":
            for dy, dx in directions:
                for k in range(1, K + 1):
                    ny, nx = i + (k * dy), j + (k * dx)
                    if 0 <= ny < N and 0 <= nx < M:
                        if arr[ny][nx] == "_":
                            arr[ny][nx] = "%"
                        if arr[ny][nx] == "#":
                            break
            arr[i][j] = "%"
for row in arr:
    print(*row, sep="")
"""

# extra_pro_2

"""
board = [int(num) for _ in range(5) for num in input().split()]
call = [int(num) for _ in range(5) for num in input().split()]
cnt = 0

x_lst = [0] * 5
y_lst = [0] * 5
di_lst1 = [0] * 10
di_lst2 = [0] * 10

for n in call:
    a = board.index(n)
    x, y = a // 5, a % 5
    x_lst[x] += 1
    y_lst[y] += 1
    di_lst1[x + y] += 1
    di_lst2[y - x + 4] += 1
    if x_lst[x] == 5:
        cnt += 1
    if y_lst[y] == 5:
        cnt += 1
    if di_lst1[x + y] == 5 or di_lst2[y - x + 4] == 5:
        cnt += 1
    d = 1
    if cnt == 3:
        break

"""
