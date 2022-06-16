# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:54:06 2020

@author: Rohini
"""
# Numbers with Common Greatest Factor
# Greatest factor of a number n, is the largest factor of ‘n’ excluding itself. 
# For example, greatest factor of 9 is 3, 15 is 5 and so on.

# Given two numbers, n1 and n2, write a code to check if the numbers have common 
# greatest factor. If they have common greatest factor 
# then print the factor and print ‘No’ otherwise.

# For example, 3 and 6 have common greatest factor, 3, so print 3. 
# If input is 15 and 21 then print 'No' as greatest factor of 15 is 5 and 
# greatest factor of 21 is 7.


n1 = int(input(""))
n2 = int(input(""))    

h = 0
d = 0
    
for n in range(2, n1):
    if (n1 % n == 0):
        h = n

for i in range(2, n2):
    if (n2 % i == 0):
        d = i

if (h == d):
  print(d)
else:
    print("No")