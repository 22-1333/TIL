# 1

'''
# object oriented programming (python, java, c++, javascript)
num = [10, 20]
print(sum(num))
'''

# 2

'''
class Person:
    name = "kai"


# 1. print kai
kai = Person() # create an instance - instance = class()
print(kai.name) # access class attribute - instance.class attribute


class Person:
    def say(self):
        print("Welcome!")
    
# 2. call say() method
kai = Person()
kai.say()

class Person:
    def __init__(self, name): # constructor method
        self.name = name # instance attribute
    
    def say(self): # instance method
        print(f"{self.name}~ Welcome!")

# 3. call say() method
kai = Person("kai")
kai.say()
'''

# 3

'''
# class => Car
# instance => hyundai, kia, ssangYong .....

class Car:
    model = "Sonata" # class attribute
    color = "white"

    def speedchange(self, v):
        print(f"speed : {v}")
        self.speed = v
    
# print Sonata, white, speed : 80
hyundai = Car()

print(hyundai.model)
print(hyundai.color)
hyundai.speedchange(80)
'''

# 4

'''
# class => Car
# instance => hyundai, kia, ssangYong .....

class Car:
    model = "Sonata" # class attribute
    color = "white"

    def speedchange(self, v):
        print(f"speed : {v}")
        self.speed = v
    
# 1. print Sonata, white, speed : 80
hyundai = Car()

print(hyundai.model)
print(hyundai.color)
hyundai.speedchange(80)

# 2. ===> constructor method
# model : Sonata, color : white, speed : 80
class Car:
    def __init__(self, model, color, speed): # constructor method
        # instance attribute
        self.model = model 
        self.color = color
        self.speed = speed

    def info(self): # instance method
        print(f"model : {self.model}, color : {self.color}, speed : {self.speed}")

hyundai = Car("Sonata", "white", 80) # instance = class()
hyundai.info() # instance.method()
'''

# 5

'''
class Singer:
    
    def __init__(self):
        self.occ = "singer"
        self.birth = "1993 May 16th"
        self.nat = "Korea"

    def rap(self):
        print("Palette")

    def dance(self):
        print("The red shoes")

    def sing(self):
        print("Meaning of you")

iu = Singer()
print(iu.occ)
print(iu.birth)
print(iu.nat)

iu.rap()
iu.dance()
iu.sing()
'''

# 6

'''
class Person():
    count = 0 # class attribute

    def __init__(self, name): # constructor
        self.name = name # instance
        Person.count += 1


# count plus one whenever instance assigned
person1 = Person("aespa")
person2 = Person("BTS")

print(Person.count)
'''

# 7

'''
print("abc".upper()) # ABC

print(str.upper("abc")) # ABC
'''

# 8

'''
class Singer:

    occ = "singer"
    birth = "1993 May 16th"
    nat = "Korea"
    
    def __init__(self):
        pass

    @classmethod
    def rap(cls):
        print(f"{cls.occ} rap 'Palette'")

    @classmethod
    def dance(cls):
        print(f"{cls.occ} dance 'The red shoes'")

    @classmethod
    def sing(cls):
        print(f"{cls.occ} sing 'Meaning of you'")

iu = Singer()

iu.rap()
iu.dance()
iu.sing()
'''

# 8

'''
class Singer:

    occ = "singer"
    birth = "1993 May 16th"
    nat = "Korea"
    
    def __init__(self):
        pass

    @staticmethod
    def rap(singer):
        print(f"{singer} rap 'Palette'")

    @staticmethod
    def dance(singer):
        print(f"{singer} dance 'The red shoes'")

    @staticmethod
    def sing(singer):
        print(f"{singer} sing 'Meaning of you'")

iu = Singer()

iu.rap("IU")
iu.dance("IU")
iu.sing("IU")
'''

# 9 

'''
class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14 * self.r ** 2
    
    def __str__(self):
        return f"[Circle] radius : {self.r}"
    
c1 = Circle(10)
c2 = Circle(1)

print(c1)
print(c2)
'''