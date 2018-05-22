# Uses python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:01:29 2018

@author: Quan_Linh
The least common multiple of two positive integers a and b is 
the least positive integer m that is divisible by both a and b.
Sources: https://en.wikipedia.org/wiki/Least_common_multiple
lcm(a,b) = (a/gcd(a,b))*b
"""
import math
def gcd(a,b):
     if b == 0:
         return a
     else:
        d = a%b
        return gcd(b,d)
         
if __name__ == "__main__":
    a, b = map(int, input().split())   
    print(math.floor(a/(gcd(a, b)))*b)
    """ Test for correctness
    assert int(28851538/(gcd(28851538, 1183019))*1183019)==1933053046
    """
