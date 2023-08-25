for test in range(10):
    tc = int(input())

    num_list = list(map(int, input().split()))

    key = [1, 2, 3, 4, 5]
    idx = 0
    while True:
        first_num = num_list.pop(0)
        if first_num - key[idx % 5] <= 0:
            num_list.append(0)
            break
        else:
            num_list.append(first_num - key[idx % 5])
            idx += 1

    print(f"#{tc}", *num_list)
