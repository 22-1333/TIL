N, M, K = map(int, input().split())
gold_list = [list(map(int, input().split())) for _ in range(M)]

queue = [(0, K)]

while queue:
    now, now_gold = queue.pop(0)

    for start, end, gold in gold_list:
        if start == now:
            if now_gold - gold >= 0:
                print(end, end=" ")
                queue.append((end, now_gold - gold))
