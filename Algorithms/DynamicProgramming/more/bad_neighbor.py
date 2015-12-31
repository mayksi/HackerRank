'''
Complete problem statement: https://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009

Paraphrasing the problem statment: Given a list of integers (representation of path graph), find the maximum weighted independent set when the list is circular
(i. e. first and the last values in the list can not be part of a single set)

Key Idea: From the original problem if you remove the contraint of circular list, it represents a problem of calculating maximum weighted independent set.
Hence, I calculate maximum weighted independent sets from the following two lists and the return the greater of the two.
    1) A max weighted set of list excluding the last element
    2) A max weighted set of list excluding the first element
'''


def maximumWeightedIndependentSet(ipArray):
    '''
    method to calculate maximum weighted independent set
    '''
    # edge cases (early return)
    if len(ipArray) == 0:
        return 0
    elif len(ipArray) == 1:
        return ipArray[0]

    # initialization
    weightsList = [0]* (len(ipArray)+1)
    weightsList[0] = 0
    weightsList[1] = ipArray[0]

    # calculation of maximum weighted independent sets
    for idx in range(1, len(ipArray)):
        weightsList[idx+1] = max(weightsList[idx-1]+ipArray[idx], weightsList[idx])

    return weightsList[-1]

def getMaxDonationAmountFromHouses(ipArray):
    '''
    Wrapper method to calculate the maximum independent weighted set from two list and return greater of the two
    '''
    return max(maximumWeightedIndependentSet(testIp[1:]), maximumWeightedIndependentSet(testIp[:-1]))


if __name__ == "__main__":
    testIp = [10, 3, 2, 5, 7, 8]
    assert 19 == getMaxDonationAmountFromHouses(testIp), "%s should return 19" % testIp

    testIp = [7, 7, 7, 7, 7, 7, 7]
    assert 21 == getMaxDonationAmountFromHouses(testIp), "%s should return 21" % testIp

    testIp = [11, 15]
    assert 15 == getMaxDonationAmountFromHouses(testIp), "%s should return 15" % testIp

    testIp = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    assert 16 == getMaxDonationAmountFromHouses(testIp), "%s should return 16" % testIp

    testIp = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,\
               6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,\
               52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
    assert 2926 == getMaxDonationAmountFromHouses(testIp), "Should return 2926" % testIp
