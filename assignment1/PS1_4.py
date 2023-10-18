# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:30:01 2023

@author: zgx
"""

import random as rd
from math import *

x=rd.randint(1,100)
print("The target money is:",x)

def Least_moves(a):
    step=0
    if a % 2==0:   
        while a % 2==0:
            step+=1
            a=a / 2
            if a % 2==0:
                continue
            else:
               if a==1:
                   break
               else:
                   a=a-1
                   step+=1
    else:
        a=a-1
        step+=1
        while a % 2==0:
            step+=1
            a=a / 2
            if a % 2==0:
                continue
            else:
               if a==1:
                   break
               else:
                   a=a-1
                   step+=1
    return step

print("The least moves are:",Least_moves(x))