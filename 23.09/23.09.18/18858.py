from bisect import bisect_left, bisect_right

N, K = map(int, input().split())
churros_list = list()
for _ in range(N):
    churros_list.append(int(input()))

churros_list.sort()

