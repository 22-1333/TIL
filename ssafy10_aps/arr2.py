N = 2  # 행의 크기
M = 4  # 열의 크기

arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
for i in range(N):
    for j in range(M):
        print(arr[i][j])

arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
for j in range(M):
    for i in range(N):
        print(arr[i][j])

arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
for i in range(N):
    for j in range(M):
        print(arr[i][j] + ((M - 2 * j) * (i % 2)))

max_v = 0
for i in range(N):
    row_total = 0  # 각 행의 합
    for j in range(M):
        row_total = arr[i][j]
    if max_v < row_total:
        max_v = row_total
