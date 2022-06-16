# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:20:38 2021

@author: Rohini
"""

def checkLevel(S,W):
    flag = 0
    flag1= 0
    
    if S in W:
        level = 0
    else:
        for i in S:
            if i not in W:
                flag = 1
                break
        if flag==0:
            for j in range(0, len(S)-1):
                if W.index(S[j])>W.index(S[j+1]):
                    level = 2
                    flag1 = 1
                    break
                elif flag1==0:
                    level = 1
        elif flag==1:
            level = -1
        
    return level
            


def ddex2(S, W):
    di = 0
    for i in S:
        di += (psdx(i,W)-psdx(i,S))
    return di

  
def psdx(x, W):
    pdx = 0
    if W.count(x)>1:
        pdx = W.index(x)
    return pdx

def derivChecker(level):
    if level==0 or level==1:
        dindex = 0
        print(dindex)
    elif level==2:
        drin1 = ddex2(S,W)
        drin2 = ddex2(W,S)
        print(drin1)
        print(drin2)
    elif level == -1:
        pass
            
#-----------------------------------------------------------------------------


S = input()
W = input()

level1 = checkLevel(S, W)
print(level1)
derivChecker(level1)

level2 = checkLevel(W,S)
print(level2)
derivChecker(level2)
    
    




            
            