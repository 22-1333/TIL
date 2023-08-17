# 5097

"""
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        arr.append(arr.pop(0))
    result = arr[0]
    print(f"#{tc} {result}")
"""

# 1255

"""
def pw(lst):
    while True:
        # 한 사이클
        for i in range(1, 6):  # 1, 2, 3, 4, 5
            num = lst.pop(0)
            lst.append(num - i)
            
            # 마지막 요소가 0이 되면 종료
            if lst[-1] <= 0:
                lst[-1] = 0
                return lst


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    numbers = list(map(int, input().split())) 
    result = password(numbers)
    print(f'#{tc}', *result)
"""

# 18437

"""
from collections import deque
arr = [
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
k = int(input())


def bfs(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in range(6):
            if arr[now][i] == 1:
                q.append(i)


bfs(k)
"""

# 18439

"""
arr = [
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0]
]
s = int(input())
used = [0] * 6


def bfs(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        print(now)
        for i in range(6):
            if used[i] == 1:
                continue
            if arr[now][i] == 1:
                used[i] = 1
                q.append(i)


used[s] = 1
bfs(s)
"""
