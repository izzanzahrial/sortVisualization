import time

def quickSort(array, drawData, timeTick):
	quickSortHelper(array, 0, len(array) - 1, drawData, timeTick)

def quickSortHelper(array, startIdx, endIdx, drawData, timeTick):
	if startIdx >= endIdx:
		return
	pivotIdx = startIdx
	leftIdx = startIdx + 1
	rightIdx = endIdx

	drawData(array, getColorArray(len(array), leftIdx, rightIdx, pivotIdx))
	time.sleep(timeTick)

	while rightIdx >= leftIdx:
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			drawData(array, getColorArray(len(array), leftIdx, rightIdx, pivotIdx))
			time.sleep(timeTick)
			swap(leftIdx, rightIdx, array)
			drawData(array, getColorArray(len(array), leftIdx, rightIdx, pivotIdx))
			time.sleep(timeTick)
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
			drawData(array, getColorArray(len(array), leftIdx, rightIdx, pivotIdx))
			time.sleep(timeTick)
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1
			drawData(array, getColorArray(len(array), leftIdx, rightIdx, pivotIdx))
			time.sleep(timeTick)
	drawData(array, getColorArray(len(array), leftIdx, rightIdx, pivotIdx))
	time.sleep(timeTick)
	swap(pivotIdx, rightIdx, array)
	drawData(array, getColorArray(len(array), leftIdx, rightIdx, pivotIdx))
	time.sleep(timeTick)
	leftSubArrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
	if leftSubArrayIsSmaller:
		quickSortHelper(array, startIdx, rightIdx - 1, drawData, timeTick)
		quickSortHelper(array, rightIdx + 1, endIdx, drawData, timeTick)
	else:
		quickSortHelper(array, rightIdx + 1, endIdx, drawData, timeTick)
		quickSortHelper(array, startIdx, rightIdx - 1, drawData, timeTick)

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

def getColorArray(array, leftIdx, rightIdx, pivotIdx):
	colorArray = []
	for i in range(array):
		# base color
		if i == pivotIdx:
			colorArray.append('red')
		elif i == leftIdx or i == rightIdx:
			colorArray.append('yellow')
		else:
			colorArray.append('black')

	return colorArray
