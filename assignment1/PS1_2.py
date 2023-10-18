# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:17:11 2023

@author: zgx
"""
import random as rd
import numpy as np

M1=np.zeros((5,10) , dtype=int) #learn np.zeros function from CSDN
M2=np.zeros((10,5) , dtype=int)
"""
for i in range(len(M1)):
    for j in range(len(M1[0])):
        M1[i,j]=rd.randint(0,50)
"""
def random_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i,j]=rd.randint(0,50)
    return a

M1=random_matrix(M1)
M2=random_matrix(M2)

def Matrix_multip(mat1,mat2):
    if len(mat1[0])==len(mat2):
        multmatrix=np.zeros((len(mat1),len(mat2[0])) , dtype=int)
        for i in range(len(multmatrix)):
            for j in range(len(multmatrix[0])):
                sum=0
                for k in range(len(mat2)):
                   sum+=mat1[i,k]*mat2[k,j]
                multmatrix[i,j]=sum
    return multmatrix
             
print(Matrix_multip(M1, M2))
