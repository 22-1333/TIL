def audience(time):
    total_audience = 0
    for T in Ti:
        total_audience += time // T

    return total_audience


N, M = map(int, input().split())
Ti = list()
for _ in range(N):
    Ti.append(int(input()))

start, end = 1, M * min(Ti)

while start <= end:
    mid = (start + end) // 2
    if audience(mid - 1) < M <= audience(mid):
        break
    else:
        if audience(mid) < M:
            start = mid + 1
        elif audience(mid) > M:
            end = mid - 1
        else:
            end = mid - 1

print(mid)
