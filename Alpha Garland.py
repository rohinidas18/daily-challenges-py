# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 08:36:25 2021

@author: Rohini
"""
# Alpha garland
# Given an alphanumeric string S, develop pseudocode and C code for printing the alpha garland 
# by processing S character by character based on the following rules:

# If the current character is an alphabet, add it to the garland.
# If the current character is a number, then the garland is extended by adding the alphabets 
# present so far in the garland in reverse form and then its original form alternatively.

# The process is repeated till the end of the string.

# For example, if the S= “ab3c1” ,then the garland is “ab baabba c cabbaabba”

# Note: The white space in the garland is given for understanding the process. 
# Actually the garland formed for this string is “abbaabbaccabbaabba”

# Input Format
# An alphanumeric string, S

# Output Format
# A string forming the alpha garland



s = str(input())
g = ""

for i in s:
    if i.isalpha() == True:
        g = g + i
    elif i.isnumeric() == True:
        temp1 = g[::-1]
        temp2 = g
        j = int(i)
        for k in range(0,j):
            if k%2==0:
                g = g + temp1
            else:
                g = g + temp2

print(g)