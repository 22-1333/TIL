T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    cnt_lst = [0] * 10
    for num in arr:
        cnt_lst[num] += 1
    max_idx = 0
    for idx in range(10):
        if cnt_lst[idx] >= cnt_lst[max_idx]:
            max_idx = idx
    print(f"#{tc} {max_idx} {cnt_lst[max_idx]}")
