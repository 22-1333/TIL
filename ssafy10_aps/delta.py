"""
3
1 2 3
4 5 6
7 8 9

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
"""

# 1

N = 3
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

max_v = 0  # 모든 원소가 0 이상이라면...
for i in range(N):  # 모든 원소 arr[i][j]에 대해...
    for j in range(N):
        s = arr[i][j]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:  # 배열을 벗어나지 않으면
                s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:  # s > max_v : X
            max_v = s

# 2

max_v = 0  # 모든 원소가 0 이상이라면...
for i in range(N):  # 모든 원소 arr[i][j]에 대해...
    for j in range(N):
        s = arr[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:  # 배열을 벗어나지 않으면
                s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:  # s > max_v : X
            max_v = s

# 3

m = int(input())

max_v = 0  # 모든 원소가 0 이상이라면...
for i in range(N):  # 모든 원소 arr[i][j]에 대해...
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]
        for k in range(4):
            for p in range(1, m):
                ni, nj = i + p * di[k], j + p * dj[k]
                if 0 <= ni < N and 0 <= nj < N:  # 배열을 벗어나지 않으면
                    s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:  # s > max_v : X
            max_v = s
