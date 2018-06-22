'''
Implementing the longest increasing subsequence with binarySearch
Goal: to find a longest increasing in O(nlogn) time

'''


def findLongestIncreasingSubsequence(nums):
    size = len(nums)
    if size < 2:
        return size
    memoz = [1] * size
    lenOfLongestIncreasingSub = 1
    for j in range(1, size):
        for i in range(j):
            if nums[i] < nums[j]:
                maxSofar = memoz[i] + 1
                if maxSofar > memoz[j]:
                    memoz[j] = maxSofar
                if lenOfLongestIncreasingSub < memoz[j]:
                    lenOfLongestIncreasingSub = memoz[j]
    return lenOfLongestIncreasingSub


'''
using n stacks the represent n piles
'''


def findLongestIncreasingSubSequencesByPatienceSorted(nums):
    size = len(nums)
    pred = []
    if size < 2:
        return size
    # using a n stack is empty at first, only on piles
    arrayOfStack = [[]]
    arrayOfStack[0].insert(0, nums[0])
    pred.insert(0, (None, nums[0]))   # there is no first back tracking
    for i in range(1, size):
        # looking for an stack index arrays
        stackIndex = binarySearch(arrayOfStack, nums[i])
        if stackIndex >= len(arrayOfStack):  # add more stack(piles)
            arrayOfStack.append([])
        arrayOfStack[stackIndex].insert(0, nums[i])
        if stackIndex == 0:
            pred.insert(0, (None, nums[i]))
        else:
            pred.insert(0, (arrayOfStack[stackIndex-1][0], nums[i]))
    res = []
    lenStack = len(arrayOfStack)
    lastNumber = arrayOfStack[lenStack-1][0]
    res.insert(0, lastNumber)
    for i in range(len(pred)):
        previous, current = pred[i]
        if previous is None and current == lastNumber:
            break
        if current == lastNumber and previous < current:
            res.insert(0, previous)
            lastNumber = previous

    return res
'''
binarySearch to find the left most stack that fits Ci 
'''


def binarySearch(nums, key):
    return binarySearchRecursive(nums, key, 0, len(nums) - 1)


def binarySearchRecursive(arrayOfStack, key, lo, hi):
    if lo > hi:
        return hi + 1   # create a new stack
    mid = (lo + hi) // 2
    # TODO continue go left until it reach to the point no more less element
    if arrayOfStack[mid][0] >= key:
        if mid > 1 and arrayOfStack[mid-1][0] >= key:
            return binarySearchRecursive(arrayOfStack, key, 0, mid - 1)
        else:
            return mid
    else:
        return binarySearchRecursive(arrayOfStack, key, mid + 1, hi)
