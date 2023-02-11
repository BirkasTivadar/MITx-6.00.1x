"""
Exercise: for exercise 3

ESTIMATED TIME TO COMPLETE: 5 minutes

3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

21
which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include input statements or define variables we will provide for you. Our automating testing will provide values so write your code in the following box assuming these variables are already defined.

Hint: Don't Use A Variable Called 'sum'
"""

osszeg = 0

for i in range(1, end + 1):
    osszeg += i

print(osszeg)
