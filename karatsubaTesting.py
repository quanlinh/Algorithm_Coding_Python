import karatsubaMultiplication as kat


def testingKaratsuba():

    assert kat.karatsubaMultiplication(1234, 567) == 1234*567

    assert kat.karatsubaMultiplication(1274, 132) == 1274*132
    assert kat.karatsubaMultiplication(12345, 678) == 12345*678
    assert kat.karatsubaMultiplication(357, 678) == 357*678
    assert kat.karatsubaMultiplication(1234, 4567) == 1234*4567
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    assert kat.karatsubaMultiplication(x, y) == x*y
    print(" ", kat.karatsubaMultiplication(x, y))
