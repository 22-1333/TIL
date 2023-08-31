"""
def f(i, n):
    if i == n:
        return
    else:
        B[i] = A[i]
        f(i + 1, n)


N = 5
A = [1, 2, 3, 4, 5]
B = [0] * N
f(0, N)
"""

"""
# if key -> return 1, else -> return 0
def f(i, n, key, arr):  # i: present, n: last, key: target
    if i == n:
        return 0  # no key
    elif arr[i] == key:
        return 1
    else:
        return f(i + 1, n, key, arr)


N = 5
A = [1, 2, 3, 4, 5]
K = 3
print(f(0, N, K, A))
"""

"""
def f(i, n):
    if i == n:
        print(p)
        return
    else:  # which number into p[i]
        for j in range(n):
            if used[j] == 0:  # if card is not used
                p[i] = card[j]
                used[j] = 1
                f(i + 1, n)
                used[j] = 0


card = list(map(int, input()))
used = [0] * 6  # check whether card is used
p = [0] * 6
f(0, 6)
"""

"""
def f(i, n, k):  # i: picked numbers, nPk
    if i == k:  # if picked k numbers -> completed
        print(p)
        return
    else:  # which number into p[i]
        for j in range(n):
            if used[j] == 0:  # if card is not used
                p[i] = card[j]
                used[j] = 1
                f(i + 1, n, k)
                used[j] = 0


card = [1, 2, 3, 4, 5]
N = 5  # in N numbers
K = 3  # pick K numbers and list up
used = [0] * N  # check whether card is used
p = [0] * K
f(0, N, K)
"""

"""
a = [3, 6, 7, 1, 5, 4]
N = 6
# for i in range(1, (1 << N) - 1):
for i in range(1, (1 << (N - 1))):  # (1 << N) // 2
    group1 = list()
    group2 = list()
    for j in range(N):
        if i & (1 << j):  # if j bit is not 0
            group1.append(a[j])
        else:
            group2.append(a[j])
    print(group1, group2) 
"""

"""
그래프 탐색 -> 완전 탐색: 문제 해결을 위해 가능한 모든 경우의 수를 탐색하는 방법
: stack, queue, DFS, BFS, 백트래킹, 분할정복, 시뮬레이션(사과 먹기, 농사)

1번 최소합: 완전 탐색 + DFS
2번 전자 카드: 완전 탐색 + 순열
"""

# 5188

"""
dir = [(0, 1), (1, 0)]


def dfs(x, y, sum_v):
    global result
    # 가지치기: 불필요한 경로를 차단 -> 조건에 맞지 않으면 탐색하지 않는다
    if sum_v >= result:
        return
    # 목표 지점에 도착한 경우
    if x == N - 1 and y == N - 1:
        if sum_v < result:
            result = sum_v
        return
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N:
            dfs(nx, ny, sum_v + arr[nx][ny])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')  # 무한대 표현, 음의 무한대 -float('inf')
    dfs(0, 0, arr[0][0])
    print(f"#{tc} {result}")
"""


# 5189

"""
def cart(cur, start, total):
    global result
    if cur == n - 1:
        result = min(result, arr[start][0] + total)
        return
    for i in range(1, n):
        if visited[i] == 0 and start != i:
            visited[i] = 1
            cart(cur + 1, i, total + arr[start][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    result = float('inf')
    cart(0, 0, 0)
    print(f"#{tc} {result}")
"""

# 1861

"""
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            for r, c in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i + r < N and 0 <= j + c < N and arr[i][j] + 1 == arr[i + r][j + c]:
                    v[arr[i][j]] = 1
    start, cnt, temp = 0, 1, 2
    for i in range(len(v) - 1, -1, -1):
        if v[i] == 1:
            temp += 1
        else:
            if cnt <= temp:
                cnt = temp
                start = i + 1
            temp = 1
    print(f"#{tc} {start} {cnt}")
"""

# 그리디 알고리즘: 각 단계에서 '지금 당장 가장 좋은 선택' 을 하는 방법을 사용하는 알고리즘
# 가장 쉬운 예제: 거스름돈 -> 가장 적은 개수의 동전으로 거슬러 준다.

# 18699

"""
n, L = map(int, input().split())
leaks = list(map(int, input().split()))
# 구멍의 위치 정렬
leaks.sort()
cnt = 1
cur = leaks[0]
for i in range(1, n):
    if leaks[i] - cur < L:
        continue
    else:
        cur = leaks[i]
        cnt += 1
print(cnt)
"""

# 18700

"""

"""

n, m = map(int, input().split())
six_min = float('inf')
one_min = float('inf')
for _ in range(m):
    six_cost, one_cost = map(int, input().split())
    six_min = min(six_min, six_cost)
    one_min = min(one_min, one_cost)
if one_min * 6 < six_min:
    print(one_min * n)
else:
    buy = n // 6
    n %= 6
    if n * one_min > six_min:
        buy += 1
        print(buy * six_min)
    else:
        print(buy * six_min + one_min * n)
