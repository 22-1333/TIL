K = int(input())
clock = [12, 3, 6, 9]

for turn in range((K % 360) // 90):
    last = clock.pop()
    clock.insert(0, last)

print(f"{clock[0]} {clock[3]} {clock[1]} {clock[2]}")
