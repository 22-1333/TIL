def func(n):
    if n == 10:
        return 1
    if n == 20:
        return 3
    else:
        return func(n - 10) + 2 * func(n - 20)


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    print(f"#{tc} {func(N)}")
