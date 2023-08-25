# 4874

"""
T = int(input())
for tc in range(1, T + 1):
    forth = list(input().split())
    stack = []
    error = False
    for i in range(len(forth) - 1):
        if forth[i].isdigit():  # 숫자일 경우
            stack.append(forth[i])  # 스택에 추가
        else:  # 연산자일 경우
            try:
                b = int(stack.pop())  # 두 번째 숫자
                a = int(stack.pop())  # 첫 번째 숫자
                if forth[i] == "+":
                    ans = a + b
                elif forth[i] == "-":
                    ans = a - b
                elif forth[i] == "*":
                    ans = a * b
                elif forth[i] == "/":
                    ans = a // b
                stack.append(ans)
            except:  # 두 개의 숫자를 꺼낼 수 없는 경우
                error = True
    
    if error is True or len(stack) != 1:  # 에러 발생 or 스택에 여러 값이 남아 있는 경우
        print(f"#{tc} error")
    else:
        print(f"#{tc} {stack.pop()}")
"""

# 4875

"""
def maze():
    while stack:
        y, x = stack.pop()
        arr[y][x] = -1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 3:  # 도착점을 찾았다! -> 1 반환
                    return 1
                elif arr[ny][nx] == 0:  # 갈 수 있는 곳을 모두 stack 에 추가
                    stack.append((ny, nx))  # tuple
    return 0  # 도착점을 못 찾으면 -> 0 반환


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dy = [0, 1, 0, -1]  # 세로 이동 방향
    dx = [1, 0, -1, 0]  # 가로 이동 방향
    for y_ in range(N):
        for x_ in range(N):
            if arr[y_][x_] == 2:  # 시작점 찾기
                stack = [(y_, x_)]  # 시작점을 스택에 추가
                break
    print(f"#{tc} {maze()}")
"""

# 4880

"""
def win(x, y):
    if arr[x] == arr[y]:
        return x
    elif arr[x] - arr[y] == 1 or arr[x] - arr[y] == -2:
        return x
    return y


def group(start, end):
    if start == end:
        return start
    left = group(start, (start + end) // 2)
    right = group((start + end) // 2 + 1, end)

    return win(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = group(0, N - 1) + 1
    print(f"#{tc} {result}")
"""

# 18417

"""
import copy

N, M = map(int, input().split())
lst = list(map(int, input().split()))
path = []
used = [0] * N
Min = 21e8
result = []


def dfs(level, s):
    global Min, path, result
    if level == M:
        if s < Min:
            Min = s
            result = copy.deepcopy(path)
        return

    for i in range(N):
        if used[i] == 1:
            continue
        path.append(lst[i])
        used[i] = 1
        dfs(level + 1, sum * lst[i])
        used[i] = 0
        path.pop()


dfs(0, 1)
result.sort()
print(*result)
"""

# 4881

"""
def dfs(idx, now_sum):
    global min_sum
    if now_sum >= min_sum:
        return
    if idx == N:
        if min_sum > now_sum:
            min_sum = now_sum
            return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            dfs(idx + 1, now_sum + arr[idx][i])
            used[i] = 0


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_sum = 21e8
    dfs(0, 0)
    print(f"#{tc} {min_sum}")
"""
