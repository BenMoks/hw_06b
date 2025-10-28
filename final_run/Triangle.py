from typing import Union
Number = Union[int, float]

def _is_integer(n: Number) -> bool:
    # Treat only ints as valid side inputs for this assignment
    return isinstance(n, int)

def classifyTriangle(a: Number, b: Number, c: Number) -> str:
    sides = (a, b, c)
    if not all(_is_integer(x) for x in sides):
        return "InvalidInput"
    if not all(x > 0 for x in sides):
        return "InvalidInput"

    x, y, z = sorted(sides)

    if x + y <= z:
        return "NotATriangle"
    if x == y == z:
        return "Equilateral"
    if x*x + y*y == z*z:
        return "Right"
    if x == y or y == z:
        return "Isosceles"
    return "Scalene"
