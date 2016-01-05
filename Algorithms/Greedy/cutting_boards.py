'''
Given size of a rectangle/square shape dimensions and the cost of cutting along each unit lenght,
find out the minimum cost in which the shape can be cut into 1x1 squares

Complete problem desciption: https://www.hackerrank.com/challenges/board-cutting
'''

HORIZONTAL_CUT = "H"
VERTICAL_CUT = "V"

def minBoardCuttingCost(hzCostList, vtCostList):
    '''
    Cost of cutting
    '''
    cutsV = 0
    cutsH = 0

    allCuttingCost = map(lambda x: (x, HORIZONTAL_CUT), hzCostList) + map(lambda x: (x, VERTICAL_CUT), vtCostList)
    allCuttingCost.sort(key = lambda x: x[0], reverse = True)

    totalCost = 0
    for costTuple in allCuttingCost:
        cost = costTuple[0]
        cutType = costTuple[1]

        if cutType == HORIZONTAL_CUT:
            totalCost += (cutsV+1) * cost
            cutsH += 1
        else:
            totalCost += (cutsH+1) * cost
            cutsV += 1
        totalCost %= (10^9+7)
    return totalCost



if __name__ == "__main__":

    fl = open("cb_ip.txt")

    testCasesCount = int(fl.readline().strip())
    for _ in range(testCasesCount):
        _ = fl.readline()
        hzCostList = map(int, fl.readline().strip().split(' '))
        vtCostList = map(int, fl.readline().strip().split(' '))
        print minBoardCuttingCost(hzCostList, vtCostList)