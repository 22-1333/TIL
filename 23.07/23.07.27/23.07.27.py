# 1

'''
# parent class
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print(f"model : {self.model}, color : {self.color}")

# child class
class CarDrive(Car):
    def speedchange(self, speed):
        self.speed = speed
        print(f"speedchange : {self.speed}")

# 1. call info method
hyundai = CarDrive("sonata", "black")
hyundai.info()

# 2. call speedchange method
hyundai.speedchange(80)
'''

# 2

'''
# class inheritance => child class(parent class)
# benefit -> child class can use attribute and method of parent method

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print(f"model : {self.model}, color : {self.color}")

class CarDrive(Car):
    def __init__(self, model, color, speed):
        # 1. super() function
        super().__init__(model, color)
        self.speed = speed

    def info(self):
        print(f"model : {self.model}, color : {self.color}, speed : {self.speed}")

# 2. call info method
hyundai = CarDrive("sonata", "black", 80)
hyundai.info()
'''

# 3

'''
class Car:
    def __init__(self, model):
        self.model = model


class Hyundai(Car):
    color = "black"
    def speed(self):
        return "80km/h"


class Kia(Car):
    color = "white"
    def engine(self):
        return "1.6turbo"


class CarDrive(Hyundai, Kia):
    def speed(self):
        return "100km/h"
    

    def power(self):
        return "1.999cc"

car = CarDrive("sonata")

# 1. call speed method
print(car.speed())

# 2. call engine method
print(car.engine())

# 3. call power method
print(car.power())

# 4. access color attribute
print(car.color)
'''

# 4

'''
# overriding

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print(f"model : {self.model}, color : {self.color}")

class CarDrive(Car):
    # 1. overriding info method
    def info(self):
        print(f"the model of this car is {self.model}")
        print(f"the color of this car is {self.color}")


# 2. call info method
hyundai = CarDrive("sonata", "black")
hyundai.info()
'''

# 5

'''
# mro()
class Car:
    def __init__(self, model):
        self.model = model


class Hyundai(Car):
    color = "black"
    def speed(self):
        return "80km/h"


class Kia(Car):
    color = "white"
    def engine(self):
        return "1.6turbo"


class CarDrive(Hyundai, Kia):
    def speed(self):
        return "100km/h"
    

    def power(self):
        return "1.999cc"

car = CarDrive("sonata")

print(CarDrive.mro())
'''

# 6

'''
# error code
def calculate_sum(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    total_sum = calculate_sum(total_sum, numbers[i])

print(f"total : {total_sum}")

# debugging
def calculate_sum(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]
total_sum = 0 # NameError

for i in range(len(numbers)):
    total_sum = calculate_sum(total_sum, numbers[i])

print(f"total : {total_sum}")
'''

# 7

'''
# exception handling
from django.shortcuts import render
from django.hppt impoprt HttpResponseNotFound

def my_view(request, post_id):
    try:
        # get post by id
        post = get_post_by_id(post_id)

    except Post.DoesNotExist:
        # if there's no post, 404 error
        return HttpResponseNotFound("cannot find the post")

    return render(request, "My_template.html", {"post" : post})
'''