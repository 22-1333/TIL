# debugging by dummy code -> dummy code as breaking point

# VS Code also possible to debug

# Baek-Jun -> silver clear -> IM clear

# 방향 배열 어려운 문제 -> 오목 문제

# 16504

"""
T = int(input())
for tc in range(T):
    # 방의 가로 길이 입력
    N = int(input())
    arr = list(map(int, input().split()))
    max_cnt = 0
    # 방의 가로 길이 만큼 반복
    for i in range(N):
        cnt = 0
        # 현재 위치의 오른쪽에 있는 모든 상자를 확인
        for j in range(i + 1, N):
            # 현재 위치의 상자가 오른쪽의 상자보다 높이가 크면
            if arr[i] > arr[j]:
                cnt += 1
        # 최댓값
        if max_cnt <= cnt:
            max_cnt = cnt
    print(f"#{tc + 1} {max_cnt}")
"""


# 4836

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 10 X 10 격자 생성
    arr = [[0] * 10 for i in range(10)]
    result = 0
    for k in range(N):
        red1, blue1, red2, blue2, color = map(int, input().split())

        for i in range(red1, red2 + 1):
            for j in range(blue1, blue2 + 1):
                arr[i][j] += color
                # 격자 값이 3이면 카운팅
                if arr[i][j] == 3:
                    result += 1
    print(f"#{tc} {result}")
"""

# extra pro 1.

"""
map_arr = [[3, 3, 5, 3, 1], [2, 2, 4, 2, 6], [4, 9, 2, 3, 4], [1, 1, 1, 1, 1], [3, 3, 5, 9, 2]]
max_result = 0
max_y = 0
max_x = 0


def sum_map(y, x):
    # 대각선의 방향
    direct = [(1, 1), (1, -1), (-1, 1), (1, -1)]
    map_result = 0
    for i, j in direct:
        dir_y = y + i
        dir_x = x + j
        if 0 <= dir_y < len(map_arr) and 0 <= dir_x <len(map_arr[0]):
            map_result += map_arr[dir_y][dir_x]
    return map_result


for m in range(len(map_arr)):
    for n in range(len(map_arr[m])):
        if sum_map(m, n) > max_result:
            max_result = sum_map(m, n)
            max_y, max_x = m, n
print(max_y, max_x)
"""

# extra pro 2.

"""
map_arr = [["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"]]


def explode(center_y, center_x):

    direct = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for i, j in direct:
        dir_y = center_y + i
        dir_x = center_x + j
        if 0 <= dir_y < len(map_arr) and 0 <= dir_x < len(map_arr[0]):
            map_arr[dir_y][dir_x] = "#"


for n in range(2):
    y, x = map(int, input().split())
    explode(y, x)

for m in map_arr:
    print(*m)
"""
