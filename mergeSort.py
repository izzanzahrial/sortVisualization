import time

def mergeSort(array, drawData, timeTick):
    if len(array) <= 1:
        return array
    auxiliaryArray = array[:]
    mergeSortHelper(array, 0, len(array)-1, auxiliaryArray, drawData, timeTick)
    return array

def mergeSortHelper(array, startIdx, endIdx, auxiliaryArray, drawData, timeTick):
    if startIdx == endIdx:
        return
    middleIdx = (startIdx + endIdx) // 2
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, array, drawData, timeTick)
    mergeSortHelper(auxiliaryArray, middleIdx+1, endIdx, array, drawData, timeTick)
    merge(array, startIdx, middleIdx, endIdx, auxiliaryArray, drawData, timeTick)

def merge(array, startIdx, middleIdx, endIdx, auxiliaryArray, drawData, timeTick):
    drawData(array, getColorArray(array, startIdx, middleIdx, endIdx))
    time.sleep(timeTick)

    i = startIdx
    x = startIdx
    y = middleIdx+1
    while x <= middleIdx and y <= endIdx:
        if auxiliaryArray[x] <= auxiliaryArray[y]:
            array[i] = auxiliaryArray[x]
            x += 1
        else:
            array[i] = auxiliaryArray[y]
            y += 1
        i += 1
    while x <= middleIdx:
        array[i] = auxiliaryArray[x]
        i += 1
        x += 1
    while y <= endIdx:
        array[i] = auxiliaryArray[y]
        i += 1
        y += 1

    drawData(array, ['green' if z >= x and z <= y else 'black' for z in range(len(array))])
    time.sleep(timeTick)

def getColorArray(array, startIdx, middleIdx, endIdx):
    colorArray = []

    for i in range(len(array)):
        if i >= startIdx and i <= endIdx:
            if i >= startIdx and i <= middleIdx:
                colorArray.append('yellow')
            else:
                colorArray.append('red')
        else:
            colorArray.append('black')

    return colorArray