"""
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

bob = 0

for i in range(len(s)):
    if s[i] == 'b' and i < len(s) - 2:
        j = i + 1
        if s[j] == 'o' and j < len(s) - 1:
            k = j + 1
            if s[k] == 'b' and k < len(s):
                bob += 1

print('Number of times bob occurs is:', bob)