"""
Exercise: eval quadratic

ESTIMATED TIME TO COMPLETE: 5 minutes

Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic .

This function takes in four numbers and returns a single number.
"""


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return a * x * x + b * x + c
