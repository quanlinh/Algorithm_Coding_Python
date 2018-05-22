# Uses python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 23:24:31 2018

@author: Quan_Linh
"""
def gcd(a,b):
     if b == 0:
         return a
     else:
        d = a%b
        return gcd(b,d)
         
if __name__ == "__main__":
    a, b = map(int, input().split())   
    print(gcd(a, b))
        
        
# bugs, it did not run for some reasons