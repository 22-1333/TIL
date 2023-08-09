array = [3, 5, 1, 9, 7]
move = 0

for _ in range(4):
    if input() == "R":
        move += 1
    else:
        move -= 1

new_array = [0, 0, 0, 0, 0]

for idx in range(len(array)):
    new_array[(idx + move) % 5] = array[idx]

print(*new_array)
