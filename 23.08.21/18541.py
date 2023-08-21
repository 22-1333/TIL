T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    reverse_sample = sample[::-1]
    check_index = -1
    is_pass = False

    for sample_number in reverse_sample:
        if check_index == -K and sample_number == passcode[check_index]:
            is_pass = True
            break
        else:
            if sample_number == passcode[check_index]:
                check_index -= 1

    if is_pass:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
