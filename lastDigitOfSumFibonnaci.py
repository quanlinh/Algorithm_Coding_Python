# Uses python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:51:46 2018

@author: Quan_Linh
"""

def lastDigitsOfSumFibonnacci(fibonacciTerm,m=10):    
    if fibonacciTerm == 0:
        return 0
    elif fibonacciTerm == 1:
        return 1
    else:
        first = 0
        second = 1
        sumOfMod10 = 1
        for i in range(fibonacciTerm-1):
            temp = first
            first = second
            second = (temp+second)%m
            sumOfMod10+=second
            if sumOfMod10 >=10:
                sumOfMod10 %= 10
            #print(sumOfMod10,end = '/')
            #print(second,end=' ')
            
        return sumOfMod10
if __name__ == "__main__":
    n = int(input())
    print(lastDigitsOfSumFibonnacci(n))