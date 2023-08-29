T = int(input())
for tc in range(1, T + 1):
    N, R = map(int, input().split())
    food_list = list(map(int, input().split()))
    is_satisfied = True
    for idx in range(len(food_list)):
        one_portion = [food_list[idx]]
        for r in range(1, R + 1):
            one_portion.append(food_list[(idx + r) % N])
            one_portion.append(food_list[(idx - r) % N])
        for food in one_portion:
            if one_portion.count(food) > 2:
                is_satisfied = False

    if is_satisfied:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")
