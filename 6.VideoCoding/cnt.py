# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:58:23 2017

@author: Jayakrishna Narra
"""

def cnt(matrix):
    count=0
    for i in range(0,8):
        for j in range(0,8):
            if matrix[i,j]!=0:
                count=count+1
    return count