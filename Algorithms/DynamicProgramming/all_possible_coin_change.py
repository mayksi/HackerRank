'''
How many different ways can you make change for an amount, given a list of coins? In this problem, your code will need to efficiently compute the answer.

Task

Write a program that, given

The amount N to make change for and the number of types M of infinitely available coins
A list of M coins - C={C1,C2,C3,..,CM}
Prints out how many different ways you can make change from the coins to STDOUT.

The problem can be formally stated:

Given a value N, if we want to make change for N cents, and we have infinite supply of each of C={C1,C2,...,CM} valued coins, how many ways can we make the change? The order of coins doesn't matter.
'''

def countCoinChange(changeTotal, coinsList):
    '''
    Method to calculate coint change for
    '''
    countCountTable = []

    # for first coin
    changeCountList = [0]
    for currentTotal in range(1, 1+changeTotal):
        changeCountList.append(1 if (currentTotal%coinsList[0] == 0) else 0)
    countCountTable.append(changeCountList)


    # for rest of the coins
    for i in range(1, len(coinsList)):
        coinVal = coinsList[i]
        changeCountList = [0]
        for currentTotal in range(1, 1+changeTotal):
            possibleWays = 1 if (currentTotal%coinVal == 0) else 0 # just using current coin
            possibleWays += countCountTable[i-1][currentTotal] # without using current coin
            for j in range(1, 1+currentTotal/coinVal): # using different quantities of current coin (1, 2, 3, .. and so on)
                possibleWays += countCountTable[i-1][currentTotal - j*coinVal]
            changeCountList.append(possibleWays)
        countCountTable.append(changeCountList)

    return countCountTable[-1][-1]

if __name__ == "__main__":

    fl = open('all_possible_coin_change_input.txt')
    testCaseCount = int(fl.readline().strip())
    for _ in range(testCaseCount):
        params = map(lambda x: int(x), fl.readline().strip().split(' '))
        coinsList = list(set(map(lambda x: int(x), fl.readline().strip().split(' '))))
        print countCoinChange(params[0], coinsList)



