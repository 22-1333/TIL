# 18868

"""
N = int(input())
cnt = 0


def func(num):
    global cnt
    if num == N:
        cnt += 1
        return
    if num > N:
        return
    for i in range(1, 4):
        func(num + i)


func(0)
print(cnt)
"""

# 18870

"""
N, M = map(int, input().split())
path = [0] * 10 # 주사위를 던져 나온 값을 저장하는 path 리스트
def printpath(level):
    print(' '.join(map(str, path[:level]))) #주사위 값을 문자열로 변환하여 공백을 넣어 출력

def roll1(level): #M=1 일때 N번 주사위 던져서 나올수 있는 모든 경우
    if level == N: #주사위를 N 번던졌다면 결과출력
        printpath(level)
        return
    for i in range(1, 7):
        path[level] = i #1. 현재 레벨의 주사위 값을 i로 설정
        roll1(level + 1)# 2. 다음 레벨로 재귀 호출
        path[level] = 0 # 3. 백트래킹 : 현재 레벨의 주사위 값을 초기화

def roll2(level): #M = 2일때
    if level == N: #주사위를 N 번던졌다면 결과출력
        printpath(level)
        return
    for i in range(1, 7):
        if level > 0 and i < path[level - 1]: #중복 제거 조건
            continue
        path[level] = i #1. 현재 레벨의 주사위 값을 i로 설정
        roll2(level + 1)# 2. 다음 레벨로 재귀 호출
        path[level] = 0 # 3. 백트래킹 : 현재 레벨의 주사위 값을 초기화
DAT = [0] * 10

def roll3(level): #M = 3일때
    if level == N: #주사위를 N 번던졌다면 결과출력
        printpath(level)
        return
    for i in range(1, 7):
        if DAT[i] == 1: #사용한 눈금은 스킵
            continue
        DAT[i] = 1 #현재 레벨에서 i 눈금 사용 체크
        path[level] = i #1. 현재 레벨의 주사위 값을 i로 설정
        roll2(level + 1)# 2. 다음 레벨로 재귀 호출
        path[level] = 0 # 3. 백트래킹 : 현재 레벨의 주사위 값을 초기화
        DAT[i] = 0 # 백트래킹 : i눈금 사용 체크 초기화

if M == 1:
    roll1(0)
elif M == 2:
    roll2(0)
elif M == 3:
    roll3(0)
"""

# 18874

"""
N = int(input())
DAT = [0] * 10
cnt = 0


def func(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for col in range(N):
        if DAT[col] == 1:
            continue
        DAT[col] = 1
        func(row + 1)
        DAT[col] = 0


func(0)
print(cnt)
"""

# 18876

"""
def dfs(idx, sum_v):
    global answer
    if answer < sum_v:
        return
    if idx >= N:
        answer = sum_v
        return
    count = station[idx]
    for i in range(count, 0, -1):
        dfs(idx + i, sum_v + 1)


T = int(input())
for tc in range(1, T + 1):
    answer = float("inf")
    station = list(map(int, input().split()))
    N = station.pop(0) - 1
    dfs(0, -1)
    print(f"#{tc} {answer}")
"""

# 18877

"""
def func(cur, total):
    global min_v
    if total > min_v:
        return
    if cur == n:
        min_v = min(min_v, total)
        return
    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        func(cur + 1, total + arr[cur][i])
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    min_v = float("inf")
    func(0, 0)
    print(f"#{tc} {min_v}")
"""

# 18882

"""
import heapq

max_heap = []
min_heap = []
mid = 500


def push(v):
    if mid > v:
        heapq.heappush(max_heap, -v)
    else:
        heapq.heappush(min_heap, v)


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    push(a)
    push(b)
    
    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, mid)
        mid = -heapq.heappop(max_heap)
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, mid)
        mid = heapq.heappop(min_heap)
    print(mid)
"""

# 18884

"""
import heapq

N = int(input())
arr = list(map(int, input().split()))
que = list()
cnt = 0
for i in range(N):
    heapq.heappush(que, [arr[i], -1])
while que:
    x, tp = heapq.heappop(que)
    if tp == 0:
        break
    cnt += 1
    
    y, tp = heapq.heappop(que)
    if tp == 0:
        break
    else:
        heapq.heappush(que, [y * 2, 0])
    cnt += 1

print(cnt)
"""
