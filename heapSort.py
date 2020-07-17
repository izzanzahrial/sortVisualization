import time

def heapSort(array, drawData, timeTick):
    buildMaxHeap(array, drawData, timeTick)
    for endIdx in reversed(range(1, len(array))):
        drawData(array, ['yellow' if x == 0 or x == endIdx else 'black' for x in range(len(array))])
        time.sleep(timeTick)
        swap(0, endIdx, array)
        drawData(array, ['yellow' if x == 0 or x == endIdx else 'black' for x in range(len(array))])
        time.sleep(timeTick)
        siftDown(0, endIdx - 1, array, drawData, timeTick)
    drawData(array, ['green' for x in range(len(array))])

def buildMaxHeap(array, drawData, timeTick):
    firstParentIdx = (len(array) - 1) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1,array,drawData, timeTick)

def siftDown(currentIdx, endIdx, heap, drawData, timeTick):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap] > heap[currentIdx]:
            drawData(heap, ['yellow' if x == idxToSwap or x == currentIdx else 'black' for x in range(len(heap))])
            time.sleep(timeTick)
            swap(currentIdx, idxToSwap, heap)
            drawData(heap, ['yellow' if x == idxToSwap or x == currentIdx else 'black' for x in range(len(heap))])
            time.sleep(timeTick)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]



