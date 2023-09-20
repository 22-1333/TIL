# 18892

"""
tree = [[-1, -1] for _ in range(1001)]
preorder = list()
inorder = list()
postorder = list()


def dfs(now):
    if now == -1:
        return

    preorder.append(now)
    dfs(tree[now][0])
    inorder.append(now)
    dfs(tree[now][1])
    postorder.append(now)


N = int(input())
for _ in range(N):
    root, left, right = map(int, input().split())
    tree[root][0] = left
    tree[root][1] = right

dfs(1)
print(" ".join(map(str, inorder)))
print(" ".join(map(str, preorder)))
print(" ".join(map(str, postorder)))
"""

# 18897

"""
n, m, target = map(int, input().split())

upv = [[] for _ in range(n + 1)]
downv = [[] for _ in range(n + 1)]

up = 1
down = 1

upused = [False] * (n + 1)
downused = [False] * (n + 1)


def updfs(node):
    global up
    for next_node in upv[node]:
        if not upused[next_node]:
            up += 1
            upused[next_node] = True
            updfs(next_node)


def downdfs(node):
    global down
    for next_node in downv[node]:
        if not downused[next_node]:
            down += 1
            downused[next_node] = True
            downdfs(next_node)


for _ in range(m):
    a, b = map(int, input().split())
    upv[b].append(a)
    downv[a].append(b)

updfs(target)
downdfs(target)

print(up)
print(n - down + 1)
"""

# 18898

"""
N, s, e = map(int, input().split())
al = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
sum_v = 0
MIN = float("inf")
MAX = float("inf")


def dfs(node, dest):
    global sum_v, MIN, MAX
    if node == dest:
        if sum_v - MAX < MIN:
            MIN = sum_v - MAX
        return
    for next in al[node]:
        if visited[next[0]] == 1:
            continue
        sum_v += next[1]
        visited[next[0]] = 1
        temp = MAX
        if next[1] > MAX:
            MAX = next[1]
        dfs(next[0], dest)
        visited[next[0]] = 0
        sum_v -= next[1]
        MAX = temp


for _ in range(N - 1):
    from_v, to_v, cost = map(int, input().split())
    al[from_v].append((to_v, cost))
    al[to_v].append((from_v, cost))

visited[s] = 1
dfs(s, e)
print(MIN if MIN != float("inf") else 0)
"""

# 1865

"""

"""
def dfs(n, items, total):
    global ans

    if total <= ans:
        return

    if n == N:
        ans= max(ans, total)
        return

    for i in range(N):
        if i not in items:
            items.append(i)
            dfs(n + 1, items, total * (arr[n][i] / 100))
            items.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    dfs(0, [], 1)
    result = round(ans * 100, 6)
    print(f"#{tc} {result}")
