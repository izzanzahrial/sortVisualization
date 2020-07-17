import time

def insertionSort(array, drawData, timeTick):
    for i in range(1,len(array)):
        j = i
        while j > 0 and array[j-1]>array[j]:
            drawData(array, ['green' if x == j or x == j - 1 else 'black' for x in range(len(array))])
            time.sleep(timeTick)
            array[j-1],array[j]=array[j],array[j-1]
            j -= 1

    drawData(array,['green' for x in range(len(array))])
