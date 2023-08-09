T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    max_cnt = 0

    for letter1 in str1:
        cnt = 0
        for letter2 in str2:
            if letter1 == letter2:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

    print(f"#{tc} {max_cnt}")
