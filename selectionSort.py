import time

def selectionSort(array, drawData, timeTick):
    for i in range(len(array)-1):
        minimum = i
        for j in range(i+1,len(array)):
            if array[j] < array[minimum]:
                minimum = j
        if minimum != i:
            drawData(array,['green' if x == i or x == minimum else 'black' for x in range(len(array))])
            time.sleep(timeTick)
            array[i],array[minimum] = array[minimum],array[i]
            drawData(array, ['green' if x == i or x == minimum else 'black' for x in range(len(array))])
            time.sleep(timeTick)
    drawData(array, ['green' for x in range(len(array))])