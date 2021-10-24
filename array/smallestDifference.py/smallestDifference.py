def min_difference(array: list, num: int):
    """
        takes an integer number and returns 
        min difference between less than the number and greater than the number.
    """
    low = 0
    high = len(array) - 1
    mid = (low + high) // 2
    while(high - low != 1):
        if array[mid] == num:
            return [0, [array[mid], num]]
        elif array[mid] > num:
            high = mid
            mid = (high + low) // 2
        else:
            low = mid
            mid = (high + low) // 2
    currentMin = abs(num - array[low])
	nums = [num, array[low]]
    for n in [array[low], array[high]]:
        if abs(num - n) < currentMin:
            currentMin = abs(num - n)
			nums = [num, n]
	return [currentMin, nums]


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

	currentMinPair = min_difference(arrayTwo, arrayOne[0])
    for num in arrayOne:
        pairs = min_difference(arrayTwo, num)
        if pairs[0] < currentMinPair[0]:
			currentMinPair = pairs

    return currentMinPair[1]

