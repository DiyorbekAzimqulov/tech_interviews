class Solution:
    """
    we use binary search since array is sorted by rotated by k
    edge cases:
    if first element is less than last element of the array then it means array is not rotated, as its 
    original, so return the last element as the maximum number

    we need to have at least 2 element in our search space. 
    if current search value's previous element is greater than it, then that previous number is the max
    if current search value is less than first element then target max is on the left
    otherwise target max is on the right
    """

    def solve(self, arr):
        if len(arr) == 1:
            return arr[0]
        if arr[0] < arr[-1]:  # it means array is not rotated
            return arr[-1]
        
        left, right = 0, len(arr)
        while left < right:  # ensure we have 2 element to search
            mid = (left + right) // 2
            if arr[mid-1] > arr[mid]:
                return arr[mid-1]
            elif arr[mid] < arr[left]:
                right = mid
            else:
                left = mid
        
nums = [6, 0, 1, 2, 3, 4, 5]
s = Solution()
print(s.solve(nums))