"""
Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""

temp = s[0]
result = temp
for i in range(1, len(s)):
    if (ord(s[i]) >= ord(s[i - 1])):
        temp += s[i]
        if len(temp) > len(result):
            result = temp
    else:
        temp = s[i]

print(result)