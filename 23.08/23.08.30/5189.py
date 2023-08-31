T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    battery_consumption_list = [list(map(int, input().split())) for _ in range(N)]
    golf_course = [n for n in range(1, N)]
    used = [0] * (N - 1)
    p = [0] * (N - 1)
    min_battery_consumption = 100 * N


    def f(i, n):
        global min_battery_consumption
        if i == n:
            formal = 0
            battery_consumption = 0
            for course in p:
                battery_consumption += battery_consumption_list[formal][course]
                formal = course
                last = course
            battery_consumption += battery_consumption_list[last][0]
            min_battery_consumption = min(min_battery_consumption, battery_consumption)
            return
        else:
            for j in range(n):
                if used[j] == 0:
                    p[i] = golf_course[j]
                    used[j] = 1
                    f(i + 1, n)
                    used[j] = 0


    f(0, N - 1)
    print(f"#{tc} {min_battery_consumption}")
