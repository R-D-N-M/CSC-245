# Part 1: Defining Functions

# Basic Function

def add_numbers(a, b):
    result = a + b
    return result


def add_lambda(a, b):
    return a + b


print(add_numbers(3, 5))  # Test
print(add_lambda(3, 5))  # Test


# Flexible Function

def join_words(*words):
    sentence = " ".join(words)
    return sentence


def join_lambda(*words):
    return " ".join(words)


print(join_words("Hello", "world", "!"))  # Test
print(join_lambda("Hello", "world", "!"))  # Test


# Recursive Function

def countdown(n):
    if n >= 0:
        print(n)
        countdown(n - 1)


countdown(5)  # Test


# Normal Function Usage

def greet(name):
    message = "Hello, " + name + "!"
    return message


print(greet("Alice"))  # Test


# Function with Default Arguments

def repeat_phrase(phrase, times=2):
    result = phrase * times
    return result


print(repeat_phrase("Hi! "))  # Test
print(repeat_phrase("Hi! ", 3))  # Test


# Higher-Order Function

def apply_function(func, value):
    return func(value)


print(apply_function(lambda x: x.upper(), "hello"))  # Test


# Part 2: Errors and Exceptions

# Handling Errors

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    finally:
        print("Division attempted")


print(safe_divide(10, 0))  # Test


# Custom Exceptions

def check_age(age):
    if type(age) != int or age < 0:
        raise ValueError("Age must be a positive integer")
    return "Valid age"


try:
    print(check_age(-5))  # Test
except ValueError as e:
    print(e)


# Handling Multiple Exceptions

def parse_int(value):
    try:
        result = int(value)
        return result
    except ValueError:
        return "Error: Invalid integer"


print(parse_int("123"))  # Test
print(parse_int("abc"))  # Test

# Part 3: Iterators

# Using Built-in Iterators

numbers = [5, 4, 3, 2, 1]
numbers_iterator = iter(numbers)
print(next(numbers_iterator))  # Test
print(next(numbers_iterator))  # Test
print(next(numbers_iterator))  # Test

# Using Generator Expressions

words = ["hello", "world", "python"]
uppercase_words = (word.upper() for word in words)
for word in uppercase_words:
    print(word)  # Test


# Custom Iterator Class

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


countdown_instance = Countdown(5)
for num in countdown_instance:
    print(num)  # Test

# Using itertools

import itertools

colors = ["red", "blue", "green"]
color_cycle = itertools.cycle(colors)
for _ in range(6):
    print(next(color_cycle))  # Test
