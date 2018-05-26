#python 3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:40:58 2018

@author: Quan_Linh
The input is the amount of money
"""
def calculateCoinChange(m,coinValue):
    numberOfCoin = int(m/coinValue)
    m            = m%coinValue
    return (m,numberOfCoin)
if __name__ == "__main__":
    m = int(input())
    numberOf10Coin = 0
    numberOf5Coin  = 0
    if m >= 10:
        m,numberOf10Coin = calculateCoinChange(m,10)
    if m >= 5:
        m,numberOf5Coin  = calculateCoinChange(m,5) 
    print(numberOf10Coin+numberOf5Coin+m)
        
    
