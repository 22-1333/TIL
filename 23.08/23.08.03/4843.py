T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    default_len = len(arr)
    arr.sort()
    special_arr = []

    while len(arr) > (default_len - 10):
        special_arr.append(arr.pop(-1))
        special_arr.append(arr.pop(0))

    list_str = ""
    for num in special_arr:
        list_str += str(num) + " "

    print(f"#{tc}", list_str)
