"""
Grader

A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is:
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

Hint: What to import?
Which library should you be importing at the beginning of your code in order to call the tan function and to get the pi constant?

This is an optional exercise, but great for extra practice!
"""

import math


def polysum(n: int, s: float):
    if n < 2:
        print("It is not a polygon")
        return

    perimeter = n * s

    area = (0.25 * n * math.pow(s, 2)) / math.tan(math.pi / n)

    sum = area + math.pow(perimeter, 2)

    return round(sum, 4)
