'''
Given price trend of a stock for several days determine the maximum profit that can be made by buying selling or doing nothing with the stock
'''

BUY = -1
SELL = 1
NO_ACTION = 0



def getMaxStockProfit(priceTrend):
    '''
    Price trend for the stock
    '''

    actionTable = [NO_ACTION] * len(priceTrend)

    for idx in range(1, len(priceTrend)):
        tempIdx = idx - 1
        # buy previous stocks with lesser value
        # this will make sure that when you sell stock at current price there is always profit
        while tempIdx >= 0 and priceTrend[tempIdx] < priceTrend[idx]:
            actionTable[idx] = SELL # mark this index to SELL (all the current stock)
            actionTable[tempIdx] = BUY # mark previous stock index to BUY
            tempIdx -= 1

    # calculate profit
    stockCount = 0
    totalValue = 0
    for (idx, val) in enumerate(actionTable):

        if val == -1: # buy
            stockCount += 1
            totalValue += val*priceTrend[idx]
        elif val == 1: # sell all stocks
            totalValue += val*priceTrend[idx]*stockCount
            stockCount = 0 # reset stock count
    return totalValue

if __name__ == "__main__":

    fl = open('stock_maximize_input.txt')

    testCaseCount = int(fl.readline().strip())

    for _ in range(testCaseCount):
        fl.readline()
        priceTrend = map(lambda x: int(x), fl.readline().strip().split())
        print getMaxStockProfit(priceTrend)
