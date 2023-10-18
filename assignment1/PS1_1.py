# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def print_values(a,b,c):
    if a>b :
        if b>c :
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b>c:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
        else:
            print(c,b,a)

print_values(1,2,3)