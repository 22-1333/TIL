N, M = map(int, input().split())
market = [list(map(int, input().split())) for _ in range(M)]
min_set_price = market[0][0]
min_single_price = market[0][1]
budget = 0
for set_price, single_price in market:
    min_set_price = min(min_set_price, set_price)
    min_single_price = min(min_single_price, single_price)

vodka_set = N // 6

if min_set_price < min_single_price * (N % 6):
    budget = (vodka_set + 1) * min_set_price
else:
    budget = vodka_set * min_set_price + min_single_price * (N % 6)

print(budget)
