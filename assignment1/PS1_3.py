# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:51:09 2023

@author: zgx
"""
"""
注：aaaa
"""

import math as math

def Pascal_triangle(k):
    c=0
    if k==1:
        print(1)
    else:
        for i in range(k):
            c=math.factorial(k-1) // math.factorial(i) // math.factorial(k-1-i) #learn math.factorial（阶乘） function from CSDN
            print(int(c),end=" ")

Pascal_triangle(100)
print("\n")
Pascal_triangle(200)