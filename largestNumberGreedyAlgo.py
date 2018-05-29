#uses python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:28:30 2018

@author: Quan_Linh
fastest way to concatenate is use ''.join
https://stackoverflow.com/questions/1316887/what-is-the-most-efficient-string-concatenation-method-in-python
learned the error: 
    TypeError: can only join an iterable
ValueError: invalid literal for int() with base 10: ' '
the way to print out the list is make it be come a list
and can print it out by join.
''.join(thelist)     :)
"""
def largestNumber(digitList):
    maxSalary = []
    while digitList:
        maxDigit = 0
        for digit in digitList:            
            if greaterOrEqual(digit,maxDigit):
                maxDigit = digit       
        maxSalary.append(maxDigit)
        digitList.remove(maxDigit)
    return maxSalary
def greaterOrEqual(digit,maxDigit):
    digit    = int((str(digit))[0])
    maxDigit = int((str(maxDigit))[0])
    return digit >= maxDigit
if __name__ == "__main__":
    n = int(input())
    digitList = list(input().split())      
    print(''.join(largestNumber(digitList)))

        
        
    