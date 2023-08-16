T = int(input())
for tc in range(1, T + 1):
    N, S = map(int, input().split())
    element_list = list(map(int, input().split()))
    subset = [0] * N
    counting = 0


    def subset_function(n):
        global counting
        if n < 0:
            subset_sum = 0
            for idx in range(len(subset)):
                if subset[idx]:
                    subset_sum += element_list[idx]
            if subset_sum == S:
                counting += 1
            return
        else:
            subset[n] = 0
            subset_function(n - 1)
            subset[n] = 1
            subset_function(n - 1)


    subset_function(N - 1)
    print(f"#{tc} {counting}")
