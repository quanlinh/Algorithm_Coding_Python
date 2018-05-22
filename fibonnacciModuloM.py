# Uses python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 13:02:46 2018

@author: Quan_Linh
"""

def fibonannciModuloM(fibonacciTerm,m):    
    if fibonacciTerm == 0:
        return 0
    elif fibonacciTerm == 1:
        return 1
    else:
        first = 0
        second = 1
        for i in range(fibonacciTerm-1):
            temp = first
            first = second
            second = (temp+second)%m
        return second
if __name__ == "__main__":
    fibonacciTerm,m = map(int,input().split())
    print(fibonannciModuloM(fibonacciTerm,m))
    