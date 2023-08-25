def binary_number(number):
    if number < 2:
        return str(number)
    else:
        return binary_number(number // 2) + str(number % 2)


N = int(input())
print(binary_number(N))
