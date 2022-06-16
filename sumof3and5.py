# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 00:03:11 2020

@author: Rohini
"""

# Sum of Three’s and Five’s
# A number greater than eight can be written as sum of 3’s and 5’s. 
# Given a number, n, write a code to check if n can be written as sum 
# of only 3’s, sum of only 5’s or sum of ‘p’ number of 3’s and ‘q’ number 
# of 5’s where p is always maximum possible value.

# For example, 9 can be written as sum of only 3’s, 25 can be written as 
# sum of only 5’s.

# If n is less than 8 then print ‘Invalid input’, if a number can be 
# written as sum of only 3’s and only 5’s then consider sum of only 3’s. 
# Use number names of 3 and 5 while printing.

n = int(input())
if n<8:
    print("Invalid input")
elif n%3 == 0:
    print("Only three's")
elif n%5 == 0:
    print("Only five's")
else:
    for i in range(1, n):
        if (n-(5*i))%3 == 0:
            o = (n-(5*i))//3
            print("{} three's and {} five's".format(o,i))
            break