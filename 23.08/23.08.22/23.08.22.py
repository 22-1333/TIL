"""
def inorder(p, n):
    if p <= n:
        inorder(p * 2, N)
        print(tree[p], end='')
        inorder(p * 2 + 1, N)


T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]
    print(f"#{tc} ", end='')
    inorder(1, N)
    print()
"""

"""
def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c] < heap[c + 1]:
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
            
    return tmp


heap = [0] * 100
last = 0
"""

# 5174

"""
def sub_tree(node):
    global cnt
    for i in range(2):
        if tree[i][node]:
            cnt += 1
            n = tree[i][node]
            sub_tree(n)


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    temp = input().split()
    tree = [[0 for _ in range(E + 2)] for _ in range(2)]
    for j in range(E):
        p_node = int(temp[2 * j])
        c_node = int(temp[2 * j + 1])
        if tree[0][p_node] == 0:
            tree[0][p_node] = c_node
        else:
            tree[1][p_node] = c_node
    cnt = 1
    sub_tree(N)
    print(f"#{tc} {cnt}")
"""

# 5176

"""
def make_bst(n):
    global node
    if n <= N:
        make_bst(n * 2)
        tree[n] = node
        node += 1
        make_bst(n * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0 for i in range(N + 1)]
    node = 1
    make_bst(1)
    print(f"#{tc} {node}")
"""

# 큐 : 선입선출
# 우선순위 큐 : 데이터들 우선순위를 가지고 저장, 우선 순위가 높은 것부터 꺼냄
# 힙 : 우선순위 큐를 구현하는 트리 기반의 자료구조, 최대힙, 최소힙
# import heapq -> heapq 라이브러리를 사용하여 최소 힙을 구현
# heapq.heappush(heap, num) : num을 최소 힙 heap에 삽입
# heapq.heappop(heap) : 최소 힙 heap에서 가장 작은 값을 꺼내서 반환

# 5177

"""
import heapq
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = []
    number = map(int, input().split())
    for num in number:
        heapq.heappush(tree, num)
    sum_v = 0
    N = len(tree)
    while N:
        sum_v += tree[N - 1]
        N //= 2
    print(f"#{tc} {sum_v}")
"""

# 5178

"""
T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]
    for i in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    for i in range(N, 0, -1):
        if i // 2 > 0:
            tree[i // 2] += tree[i]
    result = tree[L]
    print(f"#{tc} {result}")
"""

# 18573

"""
import heapq
N = int(input())
K = list(map(int, input().split()))
ugly = []
heap = [1]
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)

while len(ugly) < max(K):
    n = heapq.heappop(heap)
    if n not in ugly:
        ugly.append(n)
        heapq.heappush(heap, n * 2)
        heapq.heappush(heap, n * 3)
        heapq.heappush(heap, n * 5)

for i in K:
    print(ugly[i - 1], end=" ")
"""

# 18531

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    town = [list(map(int, input().split())) for _ in range(N + 1)]
    
    y, x = 0, 0
    for i in range(N + 1):
        for j in range(N + 1):
            if town[i][j] == 2:
                y, x = i, j
    
    home = []
    for i_ in range(N + 1):
        for j_ in range(N + 1):
            if town[i_][j_] == 1:
                home.append((i_, j_))
    
    d_lst = []
    for h in home:
        D = abs(h[0] - y) ** 2 + abs(h[1] - x) ** 2
        d_lst.append(0)
    
    R = 1
    while R ** 2 < max(d_lst):
        R += 1
    print(f"#{tc} {R}")
"""

# 18532

"""
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = input().split()
    scores = []
    for _ in range(N):
        bonus = 1
        score = 0
        r = input().split()
        for i in range(M):
            if ans[i] == r[i]:
                score += bonus
                bonus += 1
            else:
                bonus = 1
        scores.append(score)
    result = max(scores) - min(scores)
    print(f"#{tc} {result}")
"""
