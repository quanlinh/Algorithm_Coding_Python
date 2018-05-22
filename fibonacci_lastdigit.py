#python 3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 22:11:57 2018

@author: Quan_Linh
"""

n = int(input())

if n == 0:
    print ('0')
elif n == 1:
    print ('1')
else:
    first = 0
    second = 1
    for i in range(n-1):
        temp = first
        first = second
        second = (temp+second)%10
    print(second)