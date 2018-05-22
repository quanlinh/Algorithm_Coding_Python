# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 12:48:52 2018

@author: Quan_Linh
"""

# Get the number of input such as 10
n = int(input())
if n >= 2:
    
    # convert each character to int, by split them by
    # empty space and put them to the array                        
    a = [int(x) for x in input().split()]
    
    if a[0] > a[1]:
        first = a[0]                            
        second = a[1]
    else:
        second = a[0]
        first = a[1]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    for i in range(n-2):
        print(a[i+2])
        if (a[i+2] > first):
            second = first
            first = a[i+2]
        elif(a[i+2] > second):
            second = a[i+2]
                            
    print(first*second)        

