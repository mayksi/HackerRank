'''
Problem statement: https://community.topcoder.com/stat?c=problem_statement&pm=1918&rd=5006
'''

def arrangeGarden(ipList):
    '''
    '''
    arrangedList = []

    # sort the plant in increasing order of their bloom time
    ipList.sort(key = lambda x: x[2])

    # based on sorted index, create plant groups
    # a group includes all the plants that have overlapping time intervals
    arrangedList.append([[ipList[0][0]], ipList[0][1], ipList[0][2]])
    for idx in range(1, len(ipList)):
        if ipList[idx][1] > arrangedList[-1][2]:
            arrangedList.append([[ipList[idx][0]], ipList[idx][1], ipList[idx][2]])
        else:
            arrangedList[-1][0].append(ipList[idx][0])
            if ipList[idx][2] > arrangedList[-1][2]:
                arrangedList[-1][2] = ipList[idx][2]

    # next line is doing 3 things
    #    -> extract the groups of plants that needs to be planted together
    #    -> sorting the plants within an individual group from shortest to heighest
    #    -> sort the group with maximum sum of plant height (in reverse) so that tallest plants are closest to the front of the garden
    flowersGroups = sorted(map(lambda x: sorted(x[0]), arrangedList), key = lambda x : sum(x), reverse = True)

    # merge all the groups of plants into single list and return
    return [elem for sublist in flowersGroups for elem in sublist]

if __name__ == "__main__":

    flowersList = [(7, 15, 20), (5, 1, 5), (3, 10, 15), (10, 5, 10)]
    assert [3, 5, 7, 10] == arrangeGarden(flowersList)

    flowersList = [(5, 1, 365), (4, 1, 365), (3, 1, 365), (2, 1, 365), (1, 1, 365)]
    assert [1,  2,  3,  4,  5] == arrangeGarden(flowersList)

    flowersList = [(5, 1, 4), (4, 5, 9), (3, 10, 14), (2, 15, 19), (1, 20, 24)]
    assert [5,  4,  3,  2,  1] == arrangeGarden(flowersList)

    flowersList = [(5, 1, 5), (4, 5, 10), (3, 10, 15), (2, 15, 20), (1, 20, 25)]
    assert [1,  2,  3,  4,  5] == arrangeGarden(flowersList)

    flowersList = [(5, 1, 5), (4, 5, 10), (3, 10, 14), (2, 15, 20), (1, 20, 25)]
    assert [3,  4,  5,  1,  2] == arrangeGarden(flowersList)

    flowersList = [(1, 1, 2), (4, 3, 4), (2, 3, 4), (3, 1, 2), (5, 1, 2), (6, 3, 4)]
    assert [2,  4,  6,  1,  3,  5] == arrangeGarden(flowersList)

    flowersList = [(3, 1, 4), (2, 2, 3), (5, 11, 12), (4, 10, 13)]
    assert [4,  5,  2,  3] == arrangeGarden(flowersList)
