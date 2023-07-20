# 1

'''
num = int(input("input a number : "))

# if statement

if num % 2 == 1:
# if num % 2:
    print("odd number")
else:
    print("even number")
'''

# 2

'''
# common method
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i)
print(new_list) # [1, 3, 5, 7, 9]

# list comprehension
new_list_2 = [i for i in range(10) if i % 2 == 1]
print(new_list_2) # [1, 3, 5, 7, 9]

new_list_3 = [i if 1 % 2 = 1 else str(i) for i in range(10)]
'''

# 3

'''
# dust index
dust = int(input())

if dust > 150:
    print("very unhealthy")
elif dust > 80:
    print("unhealthy")
elif dust > 30:
    print("moderate")
else:
    print("good")
    
# odd or even
num = int(input())

if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# leap year
year = int(input())

if (year % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("leap year")
else:
    print("common year")
'''

# 4

'''
# multiplication table
for i in range(2, 10):
    print(f"<{i}단>")
    for j in range(1, 10):
        print(f"{i} X {j} = {i * j}")

# isosceles right triangle
n = int(input())

for i in range(n):
    print("*" * (i + 1))
'''

# 5

'''
# continue statement
n = 0

while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# break statement
n = None

while n != "y":
    n = input(("Shall we close? (y/n)"))
    if n == "y":
        break
print("the end")

# count digits
n = int(input())
count= 0

while n > 0:
    count += 1
    n //= 10

print(count)
'''

# 6

'''
from math import sqrt
numbers = [1, 4, 9, 16, 25]
sqrt_numbers = []
print(sqrt_numbers)

for number in numbers:
    sqrt_numbers.append(int(sqrt(number)))

print(sqrt_numbers)


# line comprehension
sqrt_numbers = []
print(sqrt_numbers)
print([int(sqrt(number)) for number in numbers])

# if
sqrt_numbers = []
print(sqrt_numbers)
print([int(sqrt(number)) for number in numbers if number % 2 == 0])
'''

# 7

'''
# enumerate
names = ["kai", "jane", "bob"]

for index, name in enumerate(names):
    print(f" # {index} : {name}")
'''
