T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    Ci_idx_list = [m for m in range(M)]
    fire_pit = [Ci_idx_list.pop(0) for _ in range(N)]
    cheese_idx = fire_pit.pop(0)
    cheese = Ci[cheese_idx]

    while len(fire_pit) > 1:
        if cheese == 0:
            if Ci_idx_list:
                fire_pit.append(Ci_idx_list.pop(0))
                cheese_idx = fire_pit.pop(0)
                cheese = Ci[cheese_idx]
            else:
                cheese_idx = fire_pit.pop(0)
                cheese = Ci[cheese_idx]
        else:
            fire_pit.append(cheese_idx)
            Ci[cheese_idx] = Ci[cheese_idx] // 2
            cheese_idx = fire_pit.pop(0)
            cheese = Ci[cheese_idx]

    if fire_pit:
        last_pizza = fire_pit.pop()
    else:
        last_pizza = cheese_idx

    print(last_pizza)
