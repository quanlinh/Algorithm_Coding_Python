#python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:31:59 2018

@author: Quan_Linh
"""
def fractionalSnapSack(n,totalWeight,mapValuesAndWeights):
    totalValues = 0.0
    for i in range(int(n)):
        if totalWeight == 0:
            return totalValues
        else:           
            selectValue = max(mapValuesAndWeights)
            if mapValuesAndWeights[selectValue] > 0:                            
                selectValueWeight = min(mapValuesAndWeights[selectValue],totalWeight)
                totalValues += selectValueWeight*selectValue
                mapValuesAndWeights[selectValue] -=selectValueWeight
                if mapValuesAndWeights[selectValue] == 0:
                    del mapValuesAndWeights[selectValue]
                totalWeight -= selectValueWeight
    return totalValues
if __name__ == "__main__":
    n,totalWeight = map(float,input().split())
    mapValuesAndWeights = {}
    for i in range(int(n)):
       value,weight = map(float,input().split())
       mapValuesAndWeights[value/weight] = weight
    print("%2.4f" % fractionalSnapSack(n,totalWeight,mapValuesAndWeights))    
        
    