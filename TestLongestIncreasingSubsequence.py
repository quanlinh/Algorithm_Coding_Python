import longestIncreasingSubsequence as lis


def testLongestIncreasingSubsequence():
    a = [10, 9, 2, 5, 3, 7, 101, 18]
    assert lis.findLongestIncreasingSubsequence(a) == 4
    assert lis.findLongestIncreasingSubsequence([2, 2]) == 1
    assert lis.findLongestIncreasingSubsequence([-2, -1]) == 2
    b = [7, 2, 8, 1, 3, 4, 10, 6, 9, 5]
    assert lis.findLongestIncreasingSubSequencesByPatienceSorted(b) == [1, 3, 4, 6, 9]
    assert lis.findLongestIncreasingSubSequencesByPatienceSorted(a) == [2, 3, 7, 101] or [2, 3, 7, 18]
    assert len(lis.findLongestIncreasingSubSequencesByPatienceSorted(a)) == 4
    assert len(lis.findLongestIncreasingSubSequencesByPatienceSorted([2, 2])) == 1
    assert len(lis.findLongestIncreasingSubSequencesByPatienceSorted([-2, -1])) == 2
    c = [18, 55, 66, 2, 3, 54]
    assert len(lis.findLongestIncreasingSubSequencesByPatienceSorted(c)) == 3
    d = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    assert len(lis.findLongestIncreasingSubSequencesByPatienceSorted(d)) == 6
    assert lis.findLongestIncreasingSubSequencesByPatienceSorted(d) == [1, 3, 6, 7, 9, 10]
1