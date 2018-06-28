# Uses python3
import random
import sys

'''
Python use variable binding swapping such as a,b = b, a
'''


def randomizedQuickSorted(nums):
    if len(nums) < 2:
        return
    else:
        randomizeThreeWayQuickSorted(nums, 0, len(nums) - 1)


def randomizeThreeWayQuickSorted(nums, lo, hi):
    if lo >= hi:
        return
    pivotIndex = random.randint(lo, hi)
    # swap with the left most element
    nums[pivotIndex], nums[lo] = nums[lo], nums[pivotIndex]
    leftEqual, rightEqual = threeWayPartitioning(nums, lo, hi)
    randomizeThreeWayQuickSorted(nums, lo, leftEqual)
    randomizeThreeWayQuickSorted(nums, rightEqual, hi)


def threeWayPartitioning(nums, lo, hi):
    # Assume pivot has been to swap to the left
    i = lo + 1
    lessThan = lo
    greaterThan = hi
    pivotValue = nums[lo]
    while lessThan <= i and i <= greaterThan:
        if nums[i] < pivotValue:
            nums[i], nums[lessThan] = nums[lessThan], nums[i]
            lessThan += 1
            i += 1
        elif nums[i] > pivotValue:
            nums[i], nums[greaterThan] = nums[greaterThan], nums[i]
            greaterThan -= 1
        else:
            i += 1
    return lessThan, i


if __name__ == "__main__":
    number = sys.stdin.read()
    # split the input to two part: first is n, second is a arrays of nums
    n, *nums = list(map(int, number.split()))
    randomizedQuickSorted(nums)
    for num in nums:
        print(num, end=" ")
