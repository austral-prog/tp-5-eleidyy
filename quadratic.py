import math

def roots(a, b, c):
    """Given the parameters a, b, and c, return a string representing the roots of the quadratic equation."""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"({root1:.1f}, {root2:.1f})"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"({root:.1f})"
    else:
        return "()"

def value_y(a, b, c, x):
    """Given the parameters a, b, c, and x, return the value of y for the given value of x."""
    return a*x**2 + b*x + c

def to_string(a, b, c):
    """Given the parameters a, b, and c, return a string representing the quadratic equation."""
    return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    """Given the parameters a, b, and c, return a string representing the derivative of the quadratic equation."""
    return f"f'(x) = {2*a}x + {b}"
