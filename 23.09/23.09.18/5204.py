def divide(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left = divide(arr[:middle])
        right = divide(arr[middle:])
        return merge(left, right)


def merge(left, right):
    global ans

    if right[-1] < left[-1]:
        ans += 1

    result = []
    len_l = len(left)
    len_r = len(right)
    l, r = 0, 0
    while l < len_l or r < len_r:
        if l < len_l and r < len_r:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        elif l < len_l:
            result.append(left[l])
            l += 1
        elif r < len_r:
            result.append(right[r])
            r += 1
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    result = divide(arr)
    print(f"#{tc} {result[N // 2]} {ans}")
