# 1

'''
def get_sum(num1, num2):
    return num1 + num2

num1 = 5
num2 = 3
result = get_sum(num1, num2)

print(result)

# without parameter
def get_sum_1():
    num1 = 5
    num2 = 3
    return num1 + num2

print(get_sum_1())

# without return statement
def get_sum_2(num1, num2):
    print(num1 + num2)

get_sum_2(num1, num2)
'''

# 2

'''
# positional argument
def greet(name, age):
    print(f"Hi, {name}! You are {age} years old.")

greet("Alice", 25) # Hi, Alice! You are 25 years old.

# default argument
def greet(name, age = 25):
    print(f"Hi, {name}! You are {age} years old.")

greet("Alice") # Hi, Alice! You are 25 years old.

# keyword arguments
def greet(name, age):
    print(f"Hi, {name}! You are {age} years old.")

greet(name = "Alice", age = 25) # Hi, Alice! You are 25 years old.
greet(age = 25, name = "Alice") # Hi, Alice! You are 25 years old.

# arbitrary arguments
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f"sum : {total}")

calculate_sum(1, 2, 3, 4, 5)

# arbitrary keyword arguments
def print_info(**kwargs):
    print(kwargs)

print_info(name = "Eve", age = "30", height = 175.38)
'''

# 3

'''
z = 3 # global scope

def outer():
    x = 1 
    def inner():
        y = 2 # local scope
        result = x + y # enclosed scope
        # built-in scope -> len(), print(), input()...
        print(result)
    inner()

outer()
'''

# 4

'''
a, b, c = 1, 2, 3

def enclosed():
    a, b, c = 4, 5, 6
    def local(c):
        print(a, b, c) # 4, 5, 500

    local(500)
    print(a, b, c) # 4, 5, 6

enclosed()
print(a, b, c) # 1, 2, 3

# global

a, b, c = 1, 2, 3

def enclosed():
    global a, b, c
    a, b, c = 4, 5, 6
    def local(c):
        print(a, b, c) # 4, 5, 500

    local(500)
    print(a, b, c) # 4, 5, 6

enclosed()
print(a, b, c) # 4, 5, 6
'''

# 5

'''
def factorial(num):
    # base case
    if num == 0:
        return 1

    return num * factorial(num - 1) # toward base case

n = int(input())
print(factorial(n))
'''

# 6

'''
names = ["Kai", "Jane", "Bob"]
ages = [30, 31, 27]
cities = ["Seoul", "London", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"my name is {name}, I am {age} years old and live in {city}.")
'''

# 7

'''
numbers = [1, 2, 3, 4, 5]

print(list(map(lambda x: x ** 2, numbers)))
'''

# 8

'''
packing_values = 1, 2, 3, 4, 5
print(packing_values) # (1, 2, 3, 4, 5)

numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5
'''

# 9

'''
import math
print(math.pi) # 3.141592653589793
print(math.sqrt(4)) # 2.0

from math import pi, sqrt
print(pi) # 3.141592653589793
print(sqrt(4)) # 2.0

from random import *
print(randint(1, 10)) # random number
'''

# 10

'''
import requests

url = "https://random-data-api.com/api/v2/users"
response = requests.get(url).json()

print(response)

print(response["address"]["country"])
'''