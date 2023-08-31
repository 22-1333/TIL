pay = int(input())
coins = [500, 100, 50, 10]
change = 0
for coin in coins:
    coin_change, pay = pay // coin, pay % coin
    change += coin_change

print(change)
