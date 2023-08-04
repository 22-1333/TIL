# 6485

"""
# input
# 1
# 2
# 1 3
# 2 5
# 5
# 1
# 2
# 3
# 4
# 5

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = [0] * 5001  # 1에서 5000번까지의 각 정류장을 지나는 노선수
    for _ in range(N):  # N개의 노선에 대해
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            cnt[i] += 1

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    print(f"#{tc}", end=" ")
    for x in bus_stop:
        print(cnt[x], end=" ")
    print()
"""

# 1979

"""
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0  # 단어갈 들어갈 수 있는 자리의 수
    for i in range(N):  # 행 우선 순회
        cnt = 0  # 연속한 빈칸의 개수
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            if j == N - 1 or arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
    print(ans)
"""

# 16268

"""
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]  # 터트린 풍선의 꽃가루 수
            for k in range(4):  # i, j 인접에 대해
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            if max_v < cnt:  # i, j 인접 풍선까지 더하고 나면
                max_v = cnt
    print(f"{tc} {max_v}")
"""

# 9490.

"""
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]  # 터트린 풍선의 꽃가루 수
            for k in range(4):  # i, j 인접에 대해
                for p in range(1, arr[i][j] + 1):
                    ni, nj = i + di[k] * p, j + dj[k] * p
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]  # 주변칸 풍선의 꽃가루 수
            if max_v < cnt:
                max_v = cnt
    print(f"#{tc} {max_v}")
"""

# extra_pro_2

"""

"""

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    max_area = 0
    cnt = 0

    for y in range(N):
        for x in range(N):
            cur = MAP[y][x]
            for ny in range(y, N):
                for nx in range(x, N):
                    if MAP[ny][nx] == cur:
                        area = (ny - y + 1) * (nx - x + 1)
                        if area > max_area:
                            max_area = area
                            cnt = 1
                        elif area == max_area:
                            cnt += 1

    print(f"#{tc} {cnt}")
