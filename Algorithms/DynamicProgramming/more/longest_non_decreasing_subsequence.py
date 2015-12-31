'''
Given a sequence of N numbers - A[1] , A[2] , ..., A[N]. Find the length of the longest non-decreasing sub-sequence.
'''


def longestSubsequence(ipList):
    '''
    Method to find the longest non-decreasing sub-sequence length in an unordered integer list
    '''

    lengthList = [1]*len(ipList)
    maxLength = 1
    for (idx, integer) in enumerate(ipList):
        cmpIdx = 0
        while cmpIdx < idx:
            if ipList[cmpIdx] <= ipList[idx]:
                lengthList[idx] = max(lengthList[idx], lengthList[cmpIdx]+1)
            cmpIdx += 1
        maxLength = max(maxLength, lengthList[idx])
    print lengthList
    return maxLength



print longestSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])