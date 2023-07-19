# 1

'''
a1 = 1
a2 = 2.5
a3 = 2 + 5j
a4 = "Hello World"
a5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a6 = ("2", "3", "5", "7")
a7 = range(10)
a8 = {2, 3, 5, 7}
a9 = {"a1" : 1, "a2" : 2.5, "a3" : 2 + 5j}
a10 = None
a11 = False
a12 = lambda x, y : x + y

for i in range(1, 13):
    var = f"a{i}"
    var = eval(var)
    [print(type(var))]

'''

# 2

'''
print("7 / 3 : ", 7 / 3, "\n7 // 3 : ", 7 // 3, "\n7 % 3 : ", 7 % 3)
'''

# 3

'''
print(-2 ** 4)
print(-(2 ** 4))
print((-2) ** 4)
'''

# 4

'''
degrees = 36.5
print(id(degrees))
'''

# 5

'''
number = 10
double = 2 * number
print(double)

number = 5
print(double)
'''

# 6

'''
name = "won"
age = 25
height = "175.4"
weight = "60"
is_student = True
SECOND = 10
MAX_VALUE = 100
PI = 3.141592
person_name = "Alex"


def calculate_sum(x, y):
    return x + y


def calculate_sub(x, y):
    return x - y
'''

# 7

'''
char = input()
char = input("please type a word")

num = int(input())

num = input()
num = int(num)

char1, char2 = input().split()
num1, num2 = map(int, input().split())

year, month, day = map(int, input().split("."))

num_list = list(map(int, input().split()))
'''

# 8

'''
name = input()
age = int(input())
height = float(input())

## 포맷 코드
print("my name is %s, age is %d, height is %.2f" %(name, age, height))

## f-string
print(f"my name is {name}, age is {age}, height is {height:.2f}")

## .format()
print("my name is {}, my age is {}, my height is {}" .format(name, age, height))
'''