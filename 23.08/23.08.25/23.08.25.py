# 4408

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * 201
    for a, b in arr:
        a = (a + a % 2) // 2
        b = (b + b % 2) // 2
        for i in range(min(a, b), max(a, b) + 1):
            cnt[i] += 1
    print(f"#{tc} {max(cnt)}")
"""

# 1860

"""
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = "Possible"
    for i in range(N):
        if i + 1 > arr[i] // M * K:
            result = "Impossible"
            break
    print(f"#{tc} {result}")
"""

# 4615

"""
def f(i, j, bw):
    board[i][j] = bw
    for di, dj in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
        ni, nj = i + di, j + dj
        tmp = []
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:
            tmp.append((ni, nj))
            ni, nj = ni + di, nj + dj
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for p, q in tmp:
                board[p][q] = bw


B = 1
W = 2
op = [0, 2, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2 - 1][N // 2] = B
    board[N // 2][N // 2 - 1] = B
    board[N // 2][N // 2] = W
    for col, row, bw in play:
        f(row - 1, col - 1, bw, N)
    bcnt = 0
    wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1
    print(f"#{tc} {bcnt} {wcnt}")
"""

# 1220

"""
T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    cnt = 0
    for j in range(N):
        tmp = 0
        for i in range(N):
            if arr[i][j] == 2 and tmp == 1:
                cnt += 1
                tmp = 0
            elif arr[i][j] == 1:
                tmp = 1
    print(f"#{tc} {cnt}")
"""

# 1974

"""
def check(arr):
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            row[arr[i][j]] += 1
            if row[arr[i][j]] == 2:
                return 0
            col[arr[j][i]] += 1
            if col[arr[j][j]] >= 2:
                return 0
        
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                matrix = [0] * 10
                for i in range(3):
                    for j in range(3):
                        matrix[arr[y + i][x + j]] += 1
                        if matrix[arr[y + 1][x + j]] >= 2:
                            return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = check(sudoku)
    print(f"#{tc} {result}")
"""

# 2007

"""
T = int(input())
for tc in range(1, T + 1):
    text = input()
    for i in range(1, 11):
        if text[:i] == text[i:i * 2]:
            print(f"#{tc} {i}")
            break
"""

# 3499

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = input().split()
    result = [0] * len(card)
    if N % 2:
        for i in range(N // 2 + 1):
            result[2 * i] = card[i]
        for i in range(N // 2):
            result[2 * i + 1] = card[i + N // 2 + 1]
    
    else:
        for i in range(N // 2):
            result[2 * i] = card[i]
            result[2 * i] = card[i + N // 2]
    print(f"{tc}", *result)
"""

# 4047

"""
T = int(input())
for tc in range(1, T + 1):
    card = input()
    check = []
    card_dict = {"S": 13, "D": 13, "H": 13, "C": 13}
    for i in range(0, len(card), 3):
        check.append(card[i:i + 3])
    if len(check) != len(set(check)):
        print(f"#{tc} ERROR")
    else:
        for i in range(0, len(card) - 2, 3):
            num = card_dict[card[i]]
            card_dict[card[i]] = num
        print(f"#{tc}", end=" ")
        print(*card_dict.values())
"""

# 12712

"""
def spray(y, x):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    s1 = s2 = arr[y][x]
    for i in range(4):
        for j in range(1, M):
            dy = y + directions[i][0] * j
            dx = x + directions[i][1] * j
            if 0 <= dy + y < N and 0 <= dx < N:
                s1 += arr[dy][dx]
    for i in range(4, 8):
        for j in range(1, M):
            dy = y + directions[i][0] * j
            dx = x + directions[i][1] * j
            if 0 <= dy < N and 0 < dx < N:
                s2 += arr[dy][dx]
    return max(s1, s2)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            s = spray(j, j)
            if s > max_v:
                max_v = s
    print(f"#{tc} {max_v}")
"""

# 5356

"""
T = int(input())
for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    s = [[0] * 15 for _ in range(15)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            s[i][j] = arr[i][j]
    word = ""
    for i in range(15):
        for j in range(15):
            if s[j][i] != 0:
                word += s[j][i]
    print(f"#{tc} {word}")
"""

# 16811

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))
    Ci.sort()
    can = list()
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            A = Ci[:i]
            B = Ci[i:j]
            C = Ci[j:]
            if A[-1] == B[0] or B[-1] == C[0]:
                continue
            if len(A) * len(B) * len(C) == 0:
                continue
            if len(A) > N // 2 and len(B) > N // 2 or len(C) > N // 2:
                continue
            can.append(max(abs(len(A) - len(B)), abs(len(B) - len(C)), abs(len(C) - len(A))))
    try:
        print(f"#{tc} {min(can)}")
    except NameError:
        print(f"#{tc} -1")
"""

# 2117

"""
def solve():
    ans = 0
    K = N + 1
    for k in range(K, 0, -1):
        cost = k * k + (k - 1) * (k - 1)
        for y in range(N):
            for x in range(N):
                cnt = 0
                for hy, hx in houses:
                    dist = abs(hy - y) + abs(hx - x)
                    if dist < k:
                        cnt += 1
                if cnt * M - cost >= 0:
                        ans = max(ans, cnt)
        if ans != 0:
            return ans
    return ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    houses = list()
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                houses.append((i, j))
    result = solve()
    print(f"#{tc} {result}")
"""
