T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    deck = list(input().split())
    shuffled_deck = [None] * N
    half = (N + 1) // 2

    for idx in range(N):
        if idx < half:
            shuffled_deck[idx * 2] = deck[idx]
        else:
            shuffled_deck[(idx - half) * 2 + 1] = deck[idx]

    print(f"#{tc}", *shuffled_deck)
