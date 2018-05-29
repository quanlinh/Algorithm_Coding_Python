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
slice syntax is so cool, eventhough not help much:)    
    https://docs.python.org/2/whatsnew/2.3.html#extended-slices
    
    Some interesting test cases:
        221 vs 23 => 21 vs 3 => 223 > 21
        21 vs 2 => keep if there is nothing left 1 < 2  => 221
        5678 vs 56790 => compare upto 8 vs 9. since 9 > 8, no more comparision
        need, just when they are still equals and no left digit
MO XIN in coursera have an ideas about the way compare they combine
Since there is only two ways to combine, try two of them. And which one is
greater is will be it.        
https://www.coursera.org/learn/algorithmic-toolbox/discussions/weeks/3/threads/zMgieffHEeeeShIE2GNmUA
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
    stringDigitIsGreaterOrEqual = str(digit) + str(maxDigit)
    stringMaxDigitIsGreaterOrEqual = str(maxDigit) + str(digit)
    return stringDigitIsGreaterOrEqual >= stringMaxDigitIsGreaterOrEqual
if __name__ == "__main__":
    n = int(input())
    digitList = list(input().split())   
    print(''.join(largestNumber(digitList)))

        
        
    