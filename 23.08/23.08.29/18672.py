N, M = map(int, input().split())
A = list(map(int, input().split()))
counting = 0

for i in range(N):
    for j in range(i, N):
        total = sum(A[i:j])
        if total == M:
            counting += 1

print(counting)