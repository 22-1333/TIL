N, M, X = map(int, input().split())
versus_list = [list(map(int, input().split())) for _ in range(M)]
better_than_X = 0
worse_than_X = 0


def better(me):
    global better_than_X
    for winner, loser in versus_list:
        if loser == me:
            better(winner)
            better_than_X += 1


def worse(me):
    global worse_than_X
    for winner, loser in versus_list:
        if winner == me:
            worse(loser)
            worse_than_X += 1


better(X)
worse(X)
U = min(1 + better_than_X, N - worse_than_X)
V = max(1 + better_than_X, N - worse_than_X)
print(U)
print(V)
