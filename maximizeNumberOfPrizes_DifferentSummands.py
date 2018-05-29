# uses python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 16:46:00 2018

@author: Quan_Linh
the key factors here to recognize the last numbers always to be 
greater than the the previous one. 
I was made some mistake:
    first, I try to make the last numbers is not like any number before it, 
    which is hard, and wrong
    second, I was trying to implement without fully understanding of the 
    requirements. :( which is a shame. 
I found something interesting, eventhough I used different variable names,
the inner function still now my arguments in the main function
"""
'''
    This function take the input of n numbers(candies for example)
    and return the k largerst number in which defined by
    a1 + a2 + ... + ak = n where a1 to ak is positive integer
    and 1 <= i < j <= k
'''
def maximumPrizesOfCandies(numberOfCandies):
    listOfNumbers = []
    ai = 1
    partialSum = 0
    while ai <= numberOfCandies:
        aj = numberOfCandies-(ai+partialSum)
        if ai < aj:
            listOfNumbers.append(ai)    
            partialSum+=ai
        if aj == 0:
            listOfNumbers.append(ai)
            break
        ai += 1
    return listOfNumbers
if __name__ == "__main__":
    n = int(input())
    listOfNumbers = maximumPrizesOfCandies(n)
    print(len(listOfNumbers))
    for i in range(len(listOfNumbers)):
        print(listOfNumbers[i],end=" ")