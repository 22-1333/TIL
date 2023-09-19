N = int(input())
score_list = [500]

for _ in range(N):
    score_list.extend(list(map(int, input().split())))
    score_list.sort()
    print(score_list[len(score_list) // 2])
