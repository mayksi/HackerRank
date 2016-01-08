'''
Given a message of length N + K - 1, formed by original message of length N by shifting it successively 1 position K times and XORing with the result,
find the original message

Complete details: https://www.hackerrank.com/challenges/cipher
'''


(N, K) = [185, 48]
num = '0101001101011000110011010101000111011011111110001001110101111011010001000110110010100010101101100000001001101100110010111001010111010101010110011011100101000100000011111100001010011010111010001000101011110100101100101001010111001001'


def getUnencryptedMessage(num, N, K):
    '''
    Method to unencrypt K-shifted XORed message
    '''
    # initialization
    bitList = [0]*N
    lCount = 0

    # setting starting values
    prevBit = int(num[-1])
    bitList[N-1] = prevBit

    for idx in range(N+K-3, K-2, -1):
        currBit = int(num[idx])

        lCount += 1

        if lCount < K:
            bit = prevBit ^ currBit
        else:
            bit = prevBit ^ currBit ^ bitList[N-1-lCount+K]

        prevBit = currBit
        bitList[N-1-lCount] = bit

    return ''.join(map(lambda x: str(x), bitList))

print getUnencryptedMessage(num, N, K)