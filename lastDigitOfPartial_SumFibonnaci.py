#python 3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:19:04 2018

@author: Quan_Linh
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:51:46 2018

@author: Quan_Linh
"""

def lastDigitsOfSumFibonnacci(fibonacciTermBegin,fibonacciTermBeginEnd,m=10):    
    if fibonacciTermBeginEnd == 0:
        return 0
    elif fibonacciTermBeginEnd == 1:
        return 1
    else:
        first = 0
        second = 1
        sumOfMod10 = 0
        for i in range(fibonacciTermBeginEnd-1):
            temp = first
            first = second
            second = (temp+second)%m
            # minus 2 because two first tem had been handle
            if i >= fibonacciTermBegin-2: 
             #   print(i,"i")
                sumOfMod10+=second            
            if  sumOfMod10 >=10:
                sumOfMod10 %= 10
            #print('-',sumOfMod10,end = '/')
            #print(second,end=' ')
        #print("---")    
        return sumOfMod10
if __name__ == "__main__":
    beginFibonacci,endFibonacci = map(int,input().split())
    print(lastDigitsOfSumFibonnacci(beginFibonacci,endFibonacci))