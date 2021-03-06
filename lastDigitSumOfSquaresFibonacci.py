# Uses python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:51:46 2018

@author: Quan_Linh
formula for 
F0 + F1 + F2 + ... _ Fn
sum = F(n+2) - F(2)
sum = F(n+2) - 1
The key here to using pisano period for % 10
will be 60. After that, the formula for the 
Fibonacci term can be calculate with the 
proved formula above at 
https://www.quora.com/What-is-the-sum-of-n-terms-of-a-Fibonacci-series
Finally, the last two term need to be taken for the 
edge cases that the last value is 0 - 1 would give it 
a negative. So only the first term should take into account in this cases.
The -1 here is can not be neglect since it has to do with the two last term
F(n+2) - 1 - [F(m+2)-1]

Sum of Squares of Fibonacci
F1^2 + .... Fn^2 = Fn*Fn+1
"""
def fibonannciModuloM(fibonacciTerm,m=10):    
    if fibonacciTerm == 0:
        return 0,0
    elif fibonacciTerm == 1:
        return 0,1
    else:
        first = 0
        second = 1
        for i in range(fibonacciTerm-1):
            temp = first
            first = second
            second = (temp+second)%m
        return first,second
def pisanoPeriodCal(n):
    lengthOfMod10Period = 60
    if n+2 < lengthOfMod10Period:
        first,second = fibonannciModuloM(n+2)
    else:
        simpleFibonanci = (n+2) % lengthOfMod10Period
        first,second = fibonannciModuloM(simpleFibonanci)
    if second-1 < 0 and n != 0:
        return first
    else:        
        return second-1
if __name__ == "__main__":
    n = int(input())
    if n < 60:    
        theFn,theFnPlus1 = fibonannciModuloM(n+1)            
        print((theFn*theFnPlus1) % 10)
    else:
        simpleFibonanci = (n+1)%60
        theFn,theFnPlus1 = fibonannciModuloM(simpleFibonanci)
        print((theFn*theFnPlus1) % 10)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    