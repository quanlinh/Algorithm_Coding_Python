# Uses python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 10:56:28 2018

@author: Quan_Linh
"""

#python 3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 22:11:57 2018

@author: Quan_Linh
First questions: how do we know the period to to repeat itself ? 
When we go back to 0 1 it is mean we end the period

Why is it when wrong with the input 
I totally discount the fact relation ship between the n and m
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
    
def lengthOfPisano(n,m):
    length = 2
    first = 0
    second = 1
    while True:
        temp = first
        first = second
        second = temp + second
        if second >= m:                     
            second %= m
        # as long as when the second values 
        # get to 1 and 0, we know that it will 
        # become 0 and 1 which is end the period
        if second == 0 and first == 1:
            return length
        length+=1
    return length
if __name__ == "__main__":
    n, m = map(int, input().split())
    #print(lengthOfPisano(239,1000))
   # n = 2816213588
    #m = 30524
   # n = 239
    #m = 1000
    length = lengthOfPisano(n,m)
    if length > n:
            print(fibonannciModuloM(n,m))
    else:
        simpleFibonanci = n%length
        print(fibonannciModuloM(simpleFibonanci,m))
    
