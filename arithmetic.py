import math


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def remainder(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a % b


def square(a):
    return a * a


def square_root(a):
    if a < 0:
        return "The answer is imaginary"
    return math.sqrt(a)


def exponentiation(a, b):
    return a ** b


def factorials(a):
    if a < 0 or a != int(a):
        return "Factorials are only for non-negative whole numbers"
    n = int(a)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sin(a):
    return math.sin(math.radians(a))


def cos(a):
    return math.cos(math.radians(a))


def tan(a):
    return math.tan(math.radians(a))


__all__ = [
    "addition",
    "subtraction",
    "multiplication",
    "division",
    "remainder",
    "square",
    "square_root",
    "exponentiation",
    "factorials",
    "sin",
    "cos",
    "tan",
]
