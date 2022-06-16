# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:24:35 2020

@author: Rohini
"""

# Number of Weeks to Get a Video Game
# Varun likes to get a video game of cost Rs. x, but his father doesn’t want to 
# get him immediately. So he tells varun that he will give a pockey money of Rs. p 
# every week which he can save and get the game. But varun wanted to get it faster 
# so he pleaded his father to increase the pocket money evey week by Rs. q. 
# His father agrees. Given the cost of the video game, x, pocket money initially decided p, 
# increase in pocket money every week q, write a code to find the number of weeks that 
# varun will take to get the video game.

# For example, if the cost of the video game is Rs. 100, initial pocket money agreed 
# is Rs. 20 and increase in pocket money agreed for every week is Rs. 2 then varun will 
# take 5 weeks to get the video game.


 
x = int(input())
p = int(input())
q = int(input())

amount = p
week = 1
money = p

for i in range(1, x):
    if (money <= x):
        amount = amount + q*i
        print(amount)
        money = money + amount
        print(money)
        week = week + 1
        print(week)
    else:
         break

print(week)
    