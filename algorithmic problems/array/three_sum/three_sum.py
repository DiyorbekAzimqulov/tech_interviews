# S O(nlogn)
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    results = []
    for cur in range(len(array)):
        left = cur + 1
        right = len(array) - 1
        while(left < right):
            print("sum: ", array[cur] + array[left] + array[right])
            if array[cur] + array[left] + array[right] < targetSum:
                left += 1
            elif array[cur] + array[left] + array[right] > targetSum:
                right -= 1
            else:
                results.append([array[cur], array[left], array[right]])
                left += 1
                right -= 1
    return results
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
a = threeNumberSum(array, targetSum)
print(a)