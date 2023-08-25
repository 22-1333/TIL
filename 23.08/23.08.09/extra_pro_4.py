def digit_sum(number):
    if number // 10 < 1:
        return number % 10
    else:
        return digit_sum(number // 10) + number % 10


N = int(input())
print(digit_sum(N))
