#python 3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 14:41:55 2018

@author: Quan_Linh
"""

n = int(input())
if n == 0:
    print('0')
elif n == 1:
    print('1')
else:
    first = 0
    second = 1
    # range is critical here, since we know that it start from 0
    # but we cal fibonacci number different n = 10 would be 11 count
    for i in range(n-1):
        temp = first
        first = second
        second = temp+second
    print(second)
        