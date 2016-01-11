'''
Method to do an in-place quick sort
'''

def swapElem(inputArray, pos1, pos2):
    if pos1 != pos2:
        t = inputArray[pos1]
        inputArray[pos1] = inputArray[pos2]
        inputArray[pos2] = t

def quickSort(inputArray, sIdx, eIdx):
    '''
    Method for in-place quick sort algorithm
    '''
    if sIdx >= eIdx:
        return

    pivot = inputArray[eIdx]
    partition = sIdx

    for idx in range(sIdx, eIdx):
        elem = inputArray[idx]
        if elem < pivot:
            swapElem(inputArray, partition, idx)
            partition += 1


    swapElem(inputArray, partition, eIdx)
    print " ".join(map(str, inputArray))

    quickSort(inputArray, sIdx, partition-1)
    quickSort(inputArray, partition+1, eIdx)

    return inputArray


if __name__ == "__main__":
    ipArray = [406, 157, 415, 318, 472, 46, 252, 187, 364, 481, 450, 90, 390, 35, 452, 74, 196, 312, 142, 160, 143, 220, 483, 392, 443, 488, 79, 234, 68, 150, 356, 496, 69, 88, 177, 12, 288, 120, 222, 270, 441, 422, 103, 321, 65, 316, 448, 331, 117, 183, 184, 128, 323, 141, 467, 31, 172, 48, 95, 359, 239, 209, 398, 99, 440, 171, 86, 233, 293, 162, 121, 61, 317, 52, 54, 273, 30, 226, 421, 64, 204, 444, 418, 275, 263, 108, 10, 149, 497, 20, 97, 136, 139, 200, 266, 238, 493, 22, 17, 39]
    print quickSort(ipArray, 0, 100-1)