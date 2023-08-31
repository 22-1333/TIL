N, L = map(int, input().split())
leak_point_list = list(map(int, input().split()))
leak_point_list.sort()
tape = 0
in_range = 0
for idx in range(N):
    if leak_point_list[idx] > in_range:
        tape += 1
        in_range = leak_point_list[idx] + L - 1

print(tape)
