# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:36:31 2020

@author: Rohini
"""

# Number inversions
# Rahul is facing a unique problem, which he doesn't know how to solve. The problem asks him to 
# build the smallest possible number by applying inversion on any digit of the number any number of
# times.
# Inversion of a digit is defined as that digit being replaced by 9 minus that digit. Meaning that 
# inversion of 9 will be 9 - 9 = 0 and inversion of 1 will be 9 - 1 = 8 and so on.
# The final output should not have any leading zeroes.

# Input Format:
# The only line of the input contains an integer N

# Output Format:
# Print only one single integer on a line as described above.

# Constraints:
# 1 <= N <= 10^18

# Examples:
# Input:
# 87
# Output:
# 12

# Explanation:
# 9-8 = 1
# and 9 -7 = 2
# if we see carefully, 12 is the smallest possible number we can get.
 

# Example:
# Input:
# 99
# Output:
# 90

# Explanation:
# In this case, we do not replace the first 9 since it will lead to a leading zero.

# ******************************************************************************************

N = int(input())
new = ""

if N >= 1 and N <= 10**18:
    l = list(str(N))
    if l[0] == "9":
            new = new + "9"
            for i in l[1:]:
                g = 9 - int(i)
                new = new + str(g)
    else:
        for i in l:
                g = 9 - int(i)
                if g < int(i):
                    new = new + str(g)
                else:
                    new = new + str(i)
        
print(new)