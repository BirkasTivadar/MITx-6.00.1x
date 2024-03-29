"""
Problem 3 - Using Bisection Search to Make the Program Faster

You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

The following variables contain values as described below:

1. balance - the outstanding balance on the credit card

2. annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious answer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.
"""

import sys


def fixed(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    lowerBound = (balance / 12)
    upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
    result = upperBound
    initBalance = balance

    while (upperBound - lowerBound) >= 0.003:
        monthlyFix = (lowerBound + upperBound) / 2.0
        balance = initBalance

        for i in range(12):
            balance -= monthlyFix
            balance += balance * annualInterestRate / 12

        if balance <= 0:
            result = round(monthlyFix, 2)
            upperBound = monthlyFix
        else:
            lowerBound = monthlyFix

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


teszt(fixed(320000, 0.2) == 29157.09)
teszt(fixed(999999, 0.18) == 90325.03)
teszt(fixed(166993, 0.2) == 15215.72)
teszt(fixed(424218, 0.2) == 38653.01)
teszt(fixed(449589, 0.21) == 41142.93)
teszt(fixed(95910, 0.15) == 8549.8)
teszt(fixed(258840, 0.15) == 23074.04)
teszt(fixed(31369, 0.21) == 2870.65)
teszt(fixed(346027, 0.2) == 31528.56)
teszt(fixed(340456, 0.21) == 31155.91)
teszt(fixed(238316, 0.2) == 21714.38)
teszt(fixed(357381, 0.2) == 32563.09)
