T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    A = list()


    def quick_sort(arr):
        if len(arr) == 1:
            A.append(arr[0])
            return
        elif len(arr) == 0:
            return
        else:
            pivot = arr[0]
            left, right = list(), list()
            for num in arr[1:]:
                if num <= pivot:
                    left.append(num)
                else:
                    right.append(num)

            quick_sort(left)
            A.append(pivot)
            quick_sort(right)


    quick_sort(ai)
    print(f"#{tc} {A[N // 2]}")
