"""
Problem 2 - Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

1. balance - the outstanding balance on the credit card

2. annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180
Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

import sys


def fixed(balance, annualInterestRate):
    result = (int(balance / 12 / 10)) * 10
    initBalance = balance

    while balance > 0:
        balance = initBalance
        result += 10
        for i in range(12):
            balance -= result
            balance += balance * annualInterestRate / 12

    return result


# print("Lowest Payment: ", fixed(balance, annualInterestRate))


"""
Test cases
"""


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno  # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


teszt(fixed(3329, 0.2) == 310)
teszt(fixed(4773, 0.2) == 440)
teszt(fixed(3926, 0.2) == 360)
teszt(fixed(807, 0.18) == 80)
teszt(fixed(616, 0.18) == 60)
teszt(fixed(19, 0.18) == 10)
teszt(fixed(797, 0.25) == 80)
teszt(fixed(3010, 0.04) == 260)
teszt(fixed(4291, 0.04) == 370)
teszt(fixed(4296, 0.18) == 390)
teszt(fixed(3675, 0.04) == 320)
teszt(fixed(4014, 0.04) == 350)
teszt(fixed(3929, 0.15) == 360)
teszt(fixed(3590, 0.15) == 330)
teszt(fixed(4692, 0.15) == 420)
