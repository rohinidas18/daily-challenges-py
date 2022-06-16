# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 00:19:50 2020

@author: Rohini
"""

# Beautiful Numbers
# A sequence of numbers is called cute if all the numbers in the sequence are made of only two 
# digits, 8 and 9.
# Example of a cute sequence is: 8, 9, 88, 89, 98, 99…. and so on.
# A number is called beautiful if it is divisible by any number which is part of the cute sequence.
# For example: 8 (divisible by 8), 9(divisible by 9), 889 (divisible by 889),  10668 (divisible by 
# 889) are beautiful numbers. Given a number, n, write a code to print “beautiful” 
# (without quotes) if it is divisible by any number that contains only 8 or 9 or both and print 
# -1 otherwise.

# Input Format:
# Input contains one single line denoting the number, n

# Output Format:
# Print "beautiful" if the number is a beautiful number and -1 otherwise

# Constraints:
# 1 <= N <= 999999999999999999

# n = int(input())
# N = str(n)
# invalid = True

# l = ["8", "9"]

# if n < 1 and n > 999999999999999999:
#     print("-1")
# elif 1 <= n and n <= 999999999999999999:
#     for i in N:
#         if i in l:
#             invalid = False
#     if l[0] not in N and l[1] not in N:
#         for x in range(n, 0, -1):
#             for v in str(x):
#                 if v in l:
#                     if n%x == 0:
#                         print("beautiful")
#                         break
#                     else:
#                         continue
#     if invalid == False:
#         print("beautiful")
    
    
# n = int(input())
# N = str(n)
# invalid = True

# l = ["8", "9"]

# if n < 1 or n > 999999999999999999:
#     print("-1")
# else:
#     for x in range(n, 1, -1):
#         for v in str(x):
#             if v in l:
#                 if n%x == 0:
#                     invalid = False
#                     break
#                 else:
#                     continue
#     if invalid == False:
#         print("beautiful")
        
n = int(input())
N = str(n)
invalid = True
dang = True

l = ["8", "9"]
div = []
for x in range(n, 1, -1):
        for v in str(x):
            if v in l:
                div.append(x)

if n < 1 or n > 999999999999999999:
    print("-1")
    dang = False
    
else:
    for i in div:
        if n%i == 0:
            invalid = False
            break
        else:
            continue
        
    if invalid == False and dang == True:
        print("beautiful")
    elif invalid == True:
        print("-1")
    
    
    
    
    
    
    
