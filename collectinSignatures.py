#use python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 23:17:51 2018

@author: Quan_Linh
The problems to group all students with the ages is different at 
most one, and find the minimum of these covers, so that we can 
find the minimum number of groups  to group all children different by at most
one years
The keys ideas is to recognize that this problems is a classic greedy algorithm
, it choose the earliest finish time to finish, or the the segments that have 
smallest bj
Lesson learned: becareful use of data structures that not allow duplicated keys
"""
def greedyPickOfSegment(setOfSegmentsInterval):
    # as long as the set is not all covers
    minimumNumberOfPoints = 0
    listOfPointsValues = []
    
        
    while setOfSegmentsInterval:        
        # O(n) time to get the min        
        temp1,greedyChoiceEarliest = setOfSegmentsInterval[0]
        for i in range(len(setOfSegmentsInterval)-1):
            startSegments,endSegments = setOfSegmentsInterval[i+1]
            if endSegments < greedyChoiceEarliest:
                greedyChoiceEarliest = endSegments                  
        listOfPointsValues.append(greedyChoiceEarliest)
        minimumNumberOfPoints+=1
        # remove all the incompatible interval, means remove all the 
        # segments that had been cover               
        i = 0
        while i < len(setOfSegmentsInterval):
            startSegments,endSegments = setOfSegmentsInterval[i]
            if startSegments <= greedyChoiceEarliest:
                del setOfSegmentsInterval[i]    
            else: 
                i +=1            
    return (minimumNumberOfPoints,listOfPointsValues)
    

if __name__ == "__main__":
    minimumIntervalToCollectSignatures = {}
    setOfSegmentsInterval = []
    '''
    with open('testcase3_collectSigantures.txt') as f:
        numberOfSegMents = int(f.readline())
        print(numberOfSegMents)
        for i in range(numberOfSegMents):            
            tempList =  (f.readline()).split()
            setOfSegmentsInterval.append((tempList[0],tempList[1]))
    f.close()
    '''        
    # start with an empty set
    
    numberOfSegMents = int(input())   
    for i in range(numberOfSegMents):
        ai,bj = map(int,input().split())
        setOfSegmentsInterval.append((ai,bj))
    minimumNumberOfPoints,listOfPointsValues = greedyPickOfSegment(setOfSegmentsInterval)
    print(minimumNumberOfPoints)
    for i in range(len(listOfPointsValues)):
        print(listOfPointsValues[i],end=" ")
        