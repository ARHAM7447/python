# --------------------------------------------
# 🎁 Python Decorators – Complete Overview
# --------------------------------------------

# 📘 What is a Decorator?
# A decorator is a function that modifies the behavior of another function 
# without changing its code. It takes a function as input, wraps it with additional 
# functionality, and returns the modified function.

# 🔹 Why Use Decorators?
# - Add extra behavior to functions
# - Keep code DRY (Don't Repeat Yourself)
# - Used in frameworks like Flask, Django
# - Improve modularity and readability

# -----------------------------------------------------
# 🔹 Basic Concept: Functions are first-class in Python
# -----------------------------------------------------

def greet():
    return "Hello!"

# Functions can be assigned to variables
say_hello = greet
print(say_hello())  # Output: Hello!

# ----------------------------------------
# 🔹 Basic Decorator Using @ Syntax
# ----------------------------------------

def decorator_function(original_function):
    def wrapper_function():
        print("✅ Extra BEFORE original function")
        original_function()
        print("✅ Extra AFTER original function")
    return wrapper_function

@decorator_function
def say_hello():
    print("👋 Hello!")

say_hello()

# Output:
# ✅ Extra BEFORE original function
# 👋 Hello!
# ✅ Extra AFTER original function

# ----------------------------------------
# 🔹 Decorator Without @ Syntax (Manual)
# ----------------------------------------

def greet():
    print("Hello!")

def decorator(func):
    def wrapper():
        print("Before greet")
        func()
        print("After greet")
    return wrapper

greet = decorator(greet)
greet()

# ----------------------------------------
# 🔹 Decorators with Parameters (args/kwargs)
# ----------------------------------------

def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_arguments
def add(a, b):
    return a + b

print(add(2, 3))  # Output: Calling add with (2, 3) and {} → 5

# ----------------------------------------
# 🔹 Multiple (Stacked) Decorators
# ----------------------------------------

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

print(greet())  # Output: <b><i>Hello</i></b>

# ----------------------------------------
# 🔹 Using functools.wraps to Preserve Metadata
# ----------------------------------------

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapper is running")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """This function greets."""
    print("Hello!")

print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: This function greets.

# ----------------------------------------
# 🔹 Real-World Example: Timing a Function
# ----------------------------------------

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished slow function")

slow_function()

# ----------------------------------------
# 📌 Summary:
# - @decorator is shorthand for passing function into another function
# - Use *args, **kwargs for general-purpose decorators
# - Use functools.wraps to keep function metadata
# - Decorators can be stacked for layered behavior

# ✅ Use Cases:
# - Logging
# - Authentication
# - Timing/Profiling
# - Input validation
# - Pre/post-processing
