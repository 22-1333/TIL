def number_of_churros(churros_unit):
    n = 0
    for churros in churros_list:
        n += churros // churros_unit

    return n


N, K = map(int, input().split())
churros_list = list()
for _ in range(N):
    churros_list.append(int(input()))

churros_list.sort()

if number_of_churros(churros_list[0]) < K:
    start, end = 0, churros_list[0]
else:
    start, end = churros_list[0], churros_list[-1]

while start <= end:
    mid = (start + end) // 2
    if number_of_churros(mid + 1) < K <= number_of_churros(mid):
        break
    else:
        if number_of_churros(mid) > K:
            start = mid + 1
        elif number_of_churros(mid) < K:
            end = mid - 1
        else:
            start = mid + 1

print(mid)
