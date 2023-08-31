N = int(input())
schedule_list = [list(map(int, input().split())) for _ in range(N)]
booked = [0] * N
max_conference = 0
for idx in range(N):
    if not booked[idx]:
        queue = [(idx, 1)]
        while queue:
            before_idx, conference = queue.pop(0)
            max_conference = max(max_conference, conference)
            start, end = schedule_list[before_idx]
            booked[before_idx] = 1
            for next_idx in range(0, N):
                if end <= schedule_list[next_idx][0]:
                    queue.append((next_idx, conference + 1))

print(max_conference)
