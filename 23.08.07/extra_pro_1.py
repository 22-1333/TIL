T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample_list = list(map(int, input().split()))
    pass_code_list = list(map(int, input().split()))

    pass_idx = 0
    is_pass = False

    for sample in sample_list:
        if sample == pass_code_list[pass_idx]:
            pass_idx += 1
            if pass_idx == len(pass_code_list) - 1:
                is_pass = True
                break

    print(f"#{tc} {is_pass}")
