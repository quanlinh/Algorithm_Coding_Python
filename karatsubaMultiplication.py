'''

This program taking two big integers and using karatsuba multiplication to
solved them
Since python is not limited integer we can solved it directly
Arguments: take two input as integer
'''

import math


def karatsubaMultiplication(firstNumber, secondNumber):
    firstLen = len(str(firstNumber))
    secondLen = len(str(secondNumber))

    if firstLen == 1 or secondLen == 1:
        return firstNumber * secondNumber
    else:
        lenUpperBound = max(firstLen,secondLen)
        mid = math.ceil(lenUpperBound / 2)
        mid1 = firstLen - mid
        mid2 = secondLen - mid
        aString = str(firstNumber)[:mid1]
        bString = str(firstNumber)[mid1:]
        cString = str(secondNumber)[:mid2]
        dString = str(secondNumber)[mid2:]
        if not aString or not cString:
            if not aString:
                a = 0
            else:
                a = int(aString)
            if not cString:
                c = 0
            else:
                c = int(cString)
            b = int(bString)
            d = int(dString)
            bd = karatsubaMultiplication(b, d)
            gaussTrick = karatsubaMultiplication(a+b, c+d) - bd
            return gaussTrick*10**mid + bd
        else:
            a = int(aString)
            b = int(bString)
            c = int(cString)
            d = int(dString)
            ac = karatsubaMultiplication(int(a), int(c))
            bd = karatsubaMultiplication(b, d)
            gaussTrick = karatsubaMultiplication(a+b, c+d) - ac - bd
            if lenUpperBound % 2 != 0:
                lenUpperBound += 1
            return ac*10**lenUpperBound + gaussTrick*10**mid + bd
