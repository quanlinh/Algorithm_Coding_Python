#python 3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 21:17:44 2018

@author: Quan_Linh
"""

if __name__  == "__main__":
    lengthOfList = int(input())
    profitPerClickAds   = list(map(int,input().split()))
    averageClickPerdays = list(map(int,input().split()))
    profitPerClickAds.sort()
    averageClickPerdays.sort()
    totalRevenue= 0
    for i in range(lengthOfList):        
        totalRevenue += profitPerClickAds[i]*averageClickPerdays[i]
    print(totalRevenue)
        