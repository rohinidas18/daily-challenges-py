# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 21:24:13 2020

@author: Rohini
"""

# Squeezable to Four Numbers
# Squeezing is a process in which the digits of a number is 
# squared and summed up. For example, if the number is 345 then 
# after squeezing, we get 32+42+52 = 50.

# Repeated squeezing is a process in which squeezing is 
# repeated for a number ‘n’, for some number of iteration. 
# For example, when repeated squeezing is done for two iterations for 345. 
# It looks as follows:

# # 345 -> 32+42+52 = 50
# # 50 -> 52 + 02 = 25

# # A number n, is said to squeezable to four, if it is possible to get 4 
# after a squeezing operation in number of iterations less than or equal to 10. 
# For example, 24 can be sequeezed to 4 in two iterations

# 24 -> 22 + 42 -> 20
# 20 -> 22 + 02->4

# And 500 can be sequeezed to 4 in eight iteration as shown below:

# 500-> 52 + 02 + 02 -> 25

# 25 -> 22 + 52 -> 29

# 29 -> 22 + 92 -> 85

# 85 -> 82 + 52 ->89

# 89 -> 82 + 92 -> 145

# 145 -> 12 + 42 + 52 -> 42

# 42 -> 42 + 22 -> 20

# 20 -> 22 + 02 -> 4

# Given a number, n, write a code to print the number of iterations required if 'n' 
# is squeezable to four (in number of iterations <=10) and print 'No' otherwise

# Boundary Conditions

# 4 < n <= 1000000000


n = int(input())
g = n
count = 0

if n>4 and n<= 1000000000:
    for i in range(1, 11):
        j = list(str(g))
        # print(j)
        r = 0
        for x in j:
            q = int(x)
            r += q**2
        # print(r)
        if r != 4:
            count += 1
            # print(count)
            g = r
            continue
        else:
            break

count = count + 1
if count <= 10:
    print(count)
else:
    print("No")   
    
    
    
# n=int(input())
# temp=n
# count=0

# if n>4 and n<1000000000:
#     for x in range(1, 11):
#         s1 = 0        
#         for i in range(1, len(str(temp)) + 1):
#             dig = temp%10
#             # print(dig)
#             s1=s1+dig**2
#             # print(s1)
#             temp=temp//10
#             # print(temp)
#         if s1 != 4:
#             # print(s1)
#             count = count + 1
#             # print(count)
#             temp = s1
#             continue
#         else:
#             break
    
# count=count+1    
# if(count<=10):
#     print(count)
# else:
#     print("No")  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    