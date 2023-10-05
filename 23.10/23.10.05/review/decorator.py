def prePro():
    print("pre processing")


def postPro():
    print("post processing")


def myFunc1():
    # pre processing
    prePro()
    # main processing
    print("Hi~")
    # post processing
    postPro()


def myFunc2():
    # pre processing
    prePro()
    # main processing
    print("Hi~~")
    # post processing
    postPro()


# decorator function
def my_decorator(func):
    def wrapper():
        print("pre processing")
        func()
        print("post processing")
    return wrapper


@my_decorator
def myFunc3():
    print("Hi~~~")


myFunc3()  # pre processing \ Hi ~~~ \ post processing