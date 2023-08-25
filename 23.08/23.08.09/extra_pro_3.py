def collatz(number):
    global count

    if number == 1:
        return 1
    if number % 2 == 0:
        count += 1
        return collatz(number / 2)
    else:
        count += 1
        return collatz(number * 3 + 1)


# collatz conjecture
N = int(input())
count = 0
collatz(N)

print(count)
