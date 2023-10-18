# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:19:42 2023

@author: Dawol
"""

import matplotlib.pyplot as plt

digit="123456789"

def insert_string(oldstring,char,index):
    return oldstring[:index] + char + oldstring[index:]

def insert_which_char(indicator):
    insert_char=""
    if indicator==0:
        insert_char=""
    else:
        if indicator==1:
            insert_char="+"
        elif indicator==2:
            insert_char="-"
    return insert_char

def gen_allpossible_string(string):
    all_possible_string=[]
    for i in range(3):
        char0=insert_which_char(i)
        new_string1=insert_string(string, char0, int(string.index("2")))
        for j in range(3):
            char1=insert_which_char(j)
            new_string2=insert_string(new_string1, char1, int(new_string1.index("3")))
            for k in range(3):
                char2=insert_which_char(k)
                new_string3=insert_string(new_string2, char2, int(new_string2.index("4")))
                for l in range(3):
                    char3=insert_which_char(l)
                    new_string4=insert_string(new_string3, char3, int(new_string3.index("5")))
                    for m in range(3):
                        char4=insert_which_char(m)
                        new_string5=insert_string(new_string4, char4, int(new_string4.index("6")))
                        for n in range(3):
                            char5=insert_which_char(n)
                            new_string6=insert_string(new_string5, char5, int(new_string5.index("7")))
                            for o in range(3):
                                char6=insert_which_char(o)
                                new_string7=insert_string(new_string6, char6, int(new_string6.index("8")))
                                for p in range(3):
                                    char7=insert_which_char(p)
                                    new_string8=insert_string(new_string7, char7, int(new_string7.index("9")))
                                    all_possible_string.append(new_string8)
    return all_possible_string

allpossible_string=gen_allpossible_string(digit)

def Find_expression(compare):
    expression=[]
    for elements in allpossible_string:
        result = eval(elements)
        if result==compare:
            expression.append(elements) 
    for expr in expression:
        print(expr)

target=100
Find_expression(target)
            