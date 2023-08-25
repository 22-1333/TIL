T = int(input())
for tc in range(1, T + 1):
    memory_bit = list(map(int, input()))
    initial_bit = [0] * len(memory_bit)
    fix = 0

    while initial_bit != memory_bit:
        for idx in range(len(memory_bit)):
            if initial_bit[idx] != memory_bit[idx]:
                fix += 1
                initial_bit[idx] = int(not initial_bit[idx])
                for initial_idx in range(idx + 1, len(memory_bit)):
                    initial_bit[initial_idx] = initial_bit[idx]

                break

    print(f"#{tc} {fix}")
