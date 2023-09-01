"""
def ncr(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r - 1] = a[n - 1]
        ncr(n - 1, r - 1)
        ncr(n - 1, r)


N = 5
R = 3
a = [1, 2, 3, 4, 5]
tr = [0] * R
"""

"""
def ncr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n - r + 1):
            comb[r - 1] = A[i]
            ncr(n, r - 1, i + 1)


A = [1, 2, 3, 4, 5, 6]
N = len(A)
R = 2
comb = [0] * R
ncr(N, R, 0)
"""

"""
def subset(i, n):
    if i == n:
        s = 0
        for j in range(n):
            if bit[j]:
                s += arr[j]
        if s == 0:
            for j in range(n):
                if bit[j]:
                    print(arr[j], end=" ")
            print()
    else:
        bit[i] = 1
        subset(i + 1, n)
        bit[i] = 0
        subset(i + 1, n)


arr = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
N = len(arr)
bit = [0] * N
subset(0, N)
"""

"""
def subset(i, n, s):
    if i == n:
        if s == 0:
            for j in range(n):
                if bit[j]:
                    print(arr[j], end=" ")
            print()
    else:
        subset(i + 1, n, s + arr[i])
        subset(i + 1, n, s)


arr = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
N = len(arr)
bit = [0] * N
subset(0, N)
"""

"""
N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]

meet = []
for i in range(N):
    meet.append([a[i * 2], a[i * 2 + 1]])
meet.sort(key=lambda x: x[1])
meet = [[0, 0]] + meet
print(meet)
S = []
j = 0
for i in range(1, N):
    if meet[i][0] >= meet[j][1]:
        S.append(i)
        j = 1
print(S)
"""

# 5201

"""
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    result = 0
    
    j = -1
    for i in range(M):
        while j < N - 1:
            j += 1
            if t[i] >= w[i]:
                result += w[j]
                break
    print(f"#{tc} {result}")
"""

# 5202

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])
    end, cnt = 0, 0
    for s, e in arr:
        if s >= end:
            end = 3
            cnt += 1
    print(f"#{tc} {cnt}")
"""

# 5203

"""
def check_win(cards):
    cnt = [0] * 10
    for num in cards:
        cnt[num] += 1
    if 3 in cnt:
        return True
    for i in range(8):
        if 0 not in cnt[i:i + 3]:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    all_cards = list(map(int, input().split()))
    p1 = list()
    p2 = list()
    winner = 0
    for i in range(6):
        p1.append(all_cards[i * 2])
        if len(p1) > 2 and check_win(p1):
            winner = 1
            break
        p2.append(all_cards[i * 2 + 1])
        if len(p2) > 2 and check_win(p2):
            winner = 2
            break
    print(f"#{tc} {winner}")
"""

# 18708

"""
n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 1
time = meetings[0][1]
for i in range(1, n):
    if meetings[i][0] >= time:
        cnt += 1
        time = meetings[i][1]

print(cnt)
"""

