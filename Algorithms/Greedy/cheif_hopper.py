'''
Find minimum bot energy at the starting point to complete hops over n buildings such that bot energy is never negative

Complete problem: https://www.hackerrank.com/challenges/chief-hopper
'''

def findMinStartingEnergy(buildingHtList):
    '''
    List of building heights
    '''
    lastEnergy = 0.0
    totalBuildings = len(buildingHtList)
    for idx in range(totalBuildings-1, -1, -1):
        lastEnergy = round((buildingHtList[idx]+lastEnergy)/2) # greedy criteria

    return int(lastEnergy)

if __name__ == "__main__":
    fl = open('ch_ip.txt')
    testCases = int(fl.readline().strip())
    for _ in range(testCases):
        bh = map(int, fl.readline().strip().split(' '))
        expectedOp = int(fl.readline().strip())
        actualStartEnergy = findMinStartingEnergy(bh)
        print "Calculated min start energy: %s" % actualStartEnergy
        assert actualStartEnergy == expectedOp, "Min start energy should be %s" % expectedOp