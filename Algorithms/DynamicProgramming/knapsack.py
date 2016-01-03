'''
Given a list of integers (can be selected multiple times) find the maximum sum equal to or less than a given integer M.

Problem Statement: https://www.hackerrank.com/challenges/unbounded-knapsack
'''

def getMaxSum(intList, maxSum):
    '''
    get int list max sum
    '''

    valueTable = []

    for (i, num) in enumerate(intList):

        itemValues = []
        for w in range(0, 1+maxSum):
            if num > w:
                a = valueTable[i-1][w] if i != 0 else 0
            else:

                sumList = [valueTable[i-1][w]] if i != 0 else [0]
                for j in range(1, 1+w/num):
                    sumList.append(valueTable[i-1][w-(num*j)] + num*j if i != 0 else num*j)

                a = max(sumList)
            itemValues.append(a)

        valueTable.append(itemValues)

    return valueTable[-1][-1]
if __name__ == "__main__":
    fl = open('knapsack_input.txt')
    testCaseCount = int(fl.readline().strip())

    for _ in range(testCaseCount):
        maxSum = map(lambda x: int(x), fl.readline().strip().split(' '))[1]
        intList = list(set(map(lambda x: int(x), fl.readline().strip().split(' '))))

        print getMaxSum(intList, maxSum)



