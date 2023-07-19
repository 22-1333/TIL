# 1

'''
decimal = 10
print(bin(decimal))
print(bin(decimal)[2:])
print(oct(decimal))
print(oct(decimal)[2:])
print(hex(decimal))
print(hex(decimal)[2:])
'''

# 2

'''
a = 3.2 - 3.1
b = 1.2 - 1.1

print(f"{a:.1f}")
print(f"{b:.1f}")
'''

# 3

'''
print(314e-2)
print(314 * 10 ** -2)
'''

# 4

'''
greeting = "hi"

# create 10 empty blank and fill the blank
print(f"{greeting:<10}")
print(f"{greeting:^10}")
print(f"{greeting:>10}")
'''

# 5

'''
greeting = "hello world"

# indexing
print(greeting[6])

# slicing
print(greeting[:5])
print(greeting[6:])
print(greeting[::-1])

# len
len(greeting)

# iteration
for i in range(len(greeting)):
    print(greeting[i], end = "")
print()    
for j in range(len(greeting)):
    print(greeting[j:j+1], end = "")
'''

# 6

'''
array = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

print(array[0][2]) # 3
print(array[2][0]) # 7
'''

# 7 

'''
# matrix input

rows =  int(input("How many rows?"))
matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# in a row
matrix = [list(map(int, input().split())) for _ in range(rows)]

for row in matrix:
    print(row)
'''

# 8
'''
# tuple example : direction (immutable)

def move_around(position):
    x, y = position
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # top to bottom and from side to side
    directions_2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)] # diagonal
'''

# 9

'''
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(2, 5))) # [2, 3, 4]
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]
'''

# 10

'''
my_dict = {
    "a1" : {"b1" : 1, "b2" : 2, "b3" : 3},
    "a2" : {"b1" : 4, "b2" : 5, "b3" : 6},
    "a3" : {"b1" : 7, "b2" : 8, "b3" : 9}
}

print(my_dict["a2"]["b2"]) # 5
print(my_dict.get("a2").get("b2")) #5
'''

# 11

'''
set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8, 9}

# union
print(set_1 | set_2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# difference
print(set_1 - set_2) # {1, 2, 3}

# intersection
print(set_1 & set_2) # {4, 5, 6}
'''

# 12
'''
# lottery

import random

win = set()

while len(win) != 6:
    number = random.randint(1, 45)
    win.add(number)
    print(number)

plus_number_set = win.copy()
plus_number = plus_number_set.pop()

while plus_number in win:
    plus_number = random.randint(1, 45)

for i in range(6):
    win_number = win.pop()
    print(win_number, end = " ")

print(f"+ {plus_number}")
'''

# 13

'''
print(int(float("3.5")))
'''

# 14

'''
numbers = [1, 2, 3, 4, 5]

total = 0

for num in numbers:
    total += num

print(total) # 15

# simple
print(sum(numbers)) # 15
'''

# 15

'''
vowels = "aeiou"

print(("a" and "b") in vowels) # False ("b" in vowels)
print(("b" and "a") in vowels) # True ("a" in vowels)
print(("a" or "b") in vowels) # True ("a" in vowels)
print(("b" or "a") in vowels) # False ("b" in vowels)

print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 0) # 0

print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0
'''

# 16

'''
word = "hello"
numbers = [1, 2, 3, 4, 5]

print(4 not in numbers)
print(not(4 in numbers))
'''