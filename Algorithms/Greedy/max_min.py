'''
Given a list of integers of length N and an integer K < N which represents K selected integers from the list,
find the minimum difference that can occur between max and min of selected list integers.

Detailed description: https://www.hackerrank.com/challenges/angry-children
'''

def getMinDiff(ipList, selectCount):
    '''
    Method to get the lowest possible difference between max and min for K integers
    '''    
    ipList.sort() # sort the list to arrange the list in a non-decreasing order
    
    minDiff = float('Inf')

    startPointer = 0
    while (startPointer+selectCount-1) < N:
        # compare the difference of two numbers which are at (K) positions apart and always keeing the minimum
        minDiff = min(minDiff, (ipList[startPointer+selectCount-1]-ipList[startPointer]))
        startPointer += 1
    return minDiff
    

######################################

# input
K = 3
lists = [100, 200, 300, 350, 400, 401, 402]
N = len(lists)

# output
min_diff = getMinDiff(lists, K)
print min_diff