T = int(input())

for tc in range(1, T + 1):
    STR_N = input()
    STR_M = input()

    N = len(STR_N)
    M = len(STR_M)

    is_in = False

    for m in range(M - N + 1):
        ans = 0
        for n in range(N):
            if STR_N[n] == STR_M[m + n]:
                ans += 1
        if ans == N:
            is_in = True
            break

    print(f"#{tc} {int(is_in)}")
