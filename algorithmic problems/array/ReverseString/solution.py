class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        we use two pointer technique for this problem
        we have two pointers pointing to the first and last element of the array. 
        we iterate over the array with two pointers untill our two pointers point to the same element
        in each iteration we swap first and last elements so their position reversed
        this algorithm takes O(n) time and does not use any additional space
        """
        start = 0
        end = len(s) - 1
        while start < end:
            tmp = s[end]
            s[end] = s[start]
            s[start] = tmp
            start += 1
            end -= 1
        return s
        