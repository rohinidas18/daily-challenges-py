# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:05:58 2020

@author: Rohini
"""
   
# roots of quadratic equations
   
a = int(input(""))
b = int(input(""))
c = int(input(""))

d = (b**2 - 4*a*c)
rto = ((-b) + d**(1/2))/(2*a)
rtt = ((-b) - d**(1/2))/(2*a)

print("The roots are: {} and {}".format(rto, rtt))




















