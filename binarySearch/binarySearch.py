def binarySearch(array, target):
    # Write your code here.
    l = 0
    r = len(array) - 1
    m = (l + r) // 2
    while r >= 0 and l < len(array):
        if l == r == m and array[m] != target:
            return -1
        if target == array[m]:
            return m
        elif target > array[m]:
            l = m + 1
            m = (l + r) // 2
        else:
            r = m - 1
            m = (l + r) // 2
    return -1
        

array = [1, 5, 23, 111]
target = 111
result = binarySearch(array=array, target=target)
print(result)