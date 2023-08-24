# 18611
"""
def find(node):
    if node != root[node]:
        root[node] = find(root[node])
    return root[node]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    if rank[root_x] > rank[root_y]:
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1


N = int(input())
rank = [0] * 26
root = [i for i in range(26)]
for _ in range(N):
    a, b = input().split()
    union(ord(a) - 65, ord(b) - 65)

for i in range(26):
    find(i)
DAT = [0] * 26
team = 0
for i in range(26):
    DAT[root[i]] += 1
team = 0
indi = 0
for dat in DAT:
    if data > 1:
        team += 1
    elif data == 1:
        indi += 1

print(team)
print(indi)
"""

# 1926

"""
number = int(input())
for i in range(1, number + 1):
    num = str(i)
    clap = num.count("3") + num.count("6") + num.count("9")
    
    if clap == 0:
        print(i, end=" ")
    else:
        print("-" * clap, end=" ")
"""

# 6190

"""
def check(num):
    num = str(num)
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            number = A[i] * A[j]
            if check(number):
                result = max(result, number)
        if result == 0:
            result = -1
    print(f"#{tc} {result}")
"""

# 2805

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start, end = N // 2, N // 2
    result = 0
    for i in range(N):
        for j in range(start, end + 1):
            result += arr[i][j]
        if i < N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f"#{tc} {result}")
"""

# 1220

"""
T = 10
for tc in range(1, T + 1):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        y, x = 0, j
        stack = list()
        while y < N:
            if not stack and mag[y][x] == 1:
                stack.append(1)
            elif stack and mag[y][x] == 2:
                cnt += stack.pop()
            y += 1
    print(f"#{tc} {cnt}")
"""
