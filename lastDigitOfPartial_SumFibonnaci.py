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

F(n+2) - 1 - [F(m+2)-1] = F(n+2)-F(m+2)
"""
import math
def fibonannciModuloM(fibonacciTerm,m=10):    
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
    lengthOfMod10Period = 60
    answer = None
    m,n = map(int,input().split())       
    if n+2 < lengthOfMod10Period:
        if m==n:
            answer = fibonannciModuloM(n)
        else:
            firstAnswer  =  fibonannciModuloM(n+2)
            secondAnswer = fibonannciModuloM(m+1)
            answer = firstAnswer-secondAnswer
            print(firstAnswer)
            print(secondAnswer)
    else:
        if m==n:
            simpleFibonanciFirst  =  n % lengthOfMod10Period
            answer = fibonannciModuloM(simpleFibonanciFirst)
        else:            
            simpleFibonanciFirst  =  (n+2) % lengthOfMod10Period
            simpleFibonanciSecond =  (m+1) % lengthOfMod10Period
            firstAnswer  =   fibonannciModuloM(simpleFibonanciFirst)
            secondAnswer =   fibonannciModuloM(simpleFibonanciSecond)
            answer = firstAnswer-secondAnswer
    if answer < 0:
        print(firstAnswer) 
        print(secondAnswer)
    else:
        print(answer)
 