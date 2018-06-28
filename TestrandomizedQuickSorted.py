import randomizedQuickSorted as rq
import random
import copy
def testRandomizeQuickSorted():
    empty = []
    rq.randomizedQuickSorted(empty)
    assert empty == []
    one = [1]
    rq.randomizedQuickSorted(one)
    assert one == [1]
    a1 = [2, 2, 2, 2, 2, 2, 2, 1]
    rq.randomizedQuickSorted(a1)
    assert a1 == [1, 2, 2, 2, 2, 2, 2, 2]
    # TEST BIG RANDOM NUMBERS
    tenThousands = []
    for i in range(10000):
        tenThousands.append(random.randint(0, 10000))
        # print(tenThousands[i])
    tenThousandsCopy = copy.deepcopy(tenThousands)
    tenThousandsCopy.sort()
    rq.randomizedQuickSorted(tenThousands)
    for i in range(10000):
        # print(tenThousands[i])
        assert tenThousandsCopy[i] == tenThousands[i]

