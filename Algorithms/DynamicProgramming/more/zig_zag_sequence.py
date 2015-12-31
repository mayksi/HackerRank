'''
A sequence of numbers is called a zig-zag sequence if the differences between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a zig-zag sequence.
Detailed problem statement: https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493


Key Idea: is to divide the integer list/array into sub-array of increasing or decreasing integers and count up all the sub-arrays (for any list of size > 2)

'''

import math


def getSequenceLength(inList):
    '''
    Method to calculate zig-zag lenght
    '''
    if len(inList) <= 2:
        return len(inList)

    # initialization
    countList = [1] * len(inList)
    countList[0] = 1
    countList[1] = 2
    lastSign = math.copysign(1, inList[1] - inList[0])


    # iteratively calculate sign changes (effectively counting change between increasing or decreasing contigous sequence)
    for idx in range(2, len(inList)):
        currSign = math.copysign(1, inList[idx] - inList[idx-1])
        if inList[idx] != inList[idx-1] and lastSign != currSign:
            countList[idx] = countList[idx-1] + 1
            lastSign = currSign
        else:
            countList[idx] = countList[idx-1]

    return countList[-1]


if __name__ == "__main__":
    testIp1 = [1, 7, 4, 9, 2, 5]
    assert 6 == getSequenceLength(testIp1), "Longest zig-zag sequence count should be %s" % 6

    testIp2 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    assert 7 == getSequenceLength(testIp2), "Longest zig-zag sequence count should be %s" % 7

    testIp3 = [44]
    assert 1 == getSequenceLength(testIp3), "Longest zig-zag sequence count should be %s" % 1

    testIp4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert 2 == getSequenceLength(testIp4), "Longest zig-zag sequence count should be %s" % 7

    testIp5 = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]
    assert 8 == getSequenceLength(testIp5), "Longest zig-zag sequence count should be %s" % 8

    testIp6 = [374, 40, 854, 203, 203, 156, 362, 279, 812, 955, \
               600, 947, 978, 46, 100, 953, 670, 862, 568, 188, \
               67, 669, 810, 704, 52, 861, 49, 640, 370, 908, \
               477, 245, 413, 109, 659, 401, 483, 308, 609, 120, \
               249, 22, 176, 279, 23, 22, 617, 462, 459, 244]
    assert 36 == getSequenceLength(testIp6), "Longest zig-zag sequence count should be %s" % 36
