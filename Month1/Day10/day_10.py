# Day - 10 - > DEEP DIVE: Theory: The Wrapper Patterns (Decorators)
print("Day 10: Deep Dive Exercises")

import time



print()
# DEEP DIVE - 1: Micro-Challenge: The Manual Wrapper
print("DEEP DIVE - 1: Micro-Challenge: The Manual Wrapper")

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")
say_hello = my_decorator(say_hello)
say_hello()
print()


# DEEP DIVE - 2: Micro-Challenge: The Syntactic Sugar
print("DEEP DIVE - 2: Micro-Challenge: The Syntactic Sugar")
@my_decorator
def say_hi():
    print("Hi!")
say_hi()
print()


# DEEP DIVE: 3 & 4 - Micro-Challenge: The Args Problem & The Return Value Thief
print("DEEP DIVE: 3 & 4 - Micro-Challenge: The Args Problem & The Return Value Thief")
def smart_decorator(func):
    def wrapper(*args, **kwargs):
        print("Executing function...")
        result = func(*args, **kwargs)
        return result
    return wrapper

@smart_decorator
def add(a, b):
    return a + b

print(f"Result: {add(5, 10)}")
print()



# DEEP DIVE: 5 - Micro-Challenge: The Timer (Performance)
print("DEEP DIVE: 5 - Micro-Challenge: The Timer (Performance)")

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def waste_time():
    time.sleep(1)
waste_time()
print()


# DEEP DIVE: 6 - Micro-Challenge: The Authenticator (Guard)
print("DEEP DIVE: 6 - Micro-Challenge: The Authenticator (Guard)")

role = 'guest'

def admin_required(func):
    def wrapper(*args, **kwargs):
        if role != 'admin':
            raise PermissionError("Access Denied: Admin rights required.")
        return func(*args, **kwargs)
    return wrapper

@admin_required
def delete_database():
    print("Database deleted!")
# This will raise an error because user role is 'guest' and it will "Database deleted!"
print()



# DEEP DIVE: 7 - Micro-Challenge: The Memoizer (Cache)
print("DEEP DIVE: 7 - Micro-Challenge: The Memoizer (Cache)")

def cache(func):
    storage = {}
    def wrapper(n):
        if n not in storage:
            print(f"Calculating for {n}...")
            storage[n] = func(n)
        return storage[n]
    return wrapper

@cache
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(10))
print()


# DEEP DIVE: 8 - Micro-Challenge: The Metadata Fix
print("DEEP DIVE: 8 - Micro-Challenge: The Metadata Fix")

from functools import wraps

def metadata_fix(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@metadata_fix
def secret_func():
    """I am a secret."""
    pass
print(secret_func.__name__)
print()



# DEEP DIVE: 9 - Micro-Challenge: The Stacked Decorator
print("DEEP DIVE: 9 - Micro-Challenge: The Stacked Decorator")

def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def greet():
    return "Hello"
print(greet())
print()


# DEEP DIVE: 10 - Micro-Challenge: Decorator with Arguments
print("DEEP DIVE: 10 - Micro-Challenge: Decorator with Arguments")

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Hello!")
say_hello()
print()



print("End of Day 10 Deep Dive Exercises")