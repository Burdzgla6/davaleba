# Dictionary of Functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

operations = {
    "add": add, 
    "sub": sub,
    "mul": mul,
    "div": div
}

num1 = float(input('enter first number: '))
num2 = float(input('enter second number: '))
operation = input("Choose operation: ")

if operation not in operations:
    print('invalid operation')

else:
    if operation == 'div' and num2 == 0:
        print('Cannot divide by zero')

    else:
        function = operations[operation]
        result = function(num1, num2)
        print(result)



# Greeting

def greet(func):
    def wrapper(*args, **kwargs):
        print('starting...')
        result = func(*args, **kwargs)
        if result is not None:
             print(result)
        print('done!')
        return result
    
    return wrapper

@greet
def add(a, b):
    return a + b

add(10, 5)

@greet
def introduce(name, age):
    print(f"My name is {name} and I am {age}")

introduce("Saba", 16)


# Timer 

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        execution_time = end - start

        print(f"{func.__name__} executed in {execution_time:.4f} seconds")

        return result

    return wrapper


@timer
def big_loop():
    total = 0

    for i in range(1_000_000):
        total += i

    return total


print(big_loop())


# Min age

def min_age(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            age = args[0]

            if age < limit:
                print('Access denied')
            else:
                return func(*args, **kwargs)

        return wrapper
    return decorator


@min_age(18)
def enter(age):
    print('Welcome!')


enter(16)
enter(20)


# Try again


import random

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    print(f"Attempt {i + 1} failed")

            print("All attempts failed")

        return wrapper
    return decorator


@retry(3)
def random_division():
    num1 = random.randint(1, 10)
    num2 = random.randint(0, 2)

    return num1 / num2


print(random_division())
